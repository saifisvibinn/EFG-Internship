import pandas as pd
import os

def transform_institutional_data(
    input_path='institutional_foreign_data.csv',
    output_path='institutional_foreign_clean.csv'
):
    """
    Transforms the raw institutional_foreign_data.csv (which has a messy multi-row
    header and pre-calculated totals) into a clean, flat table for Power BI.

    Output columns:
        Timestamp | Demographic | Investor_Type | Buy (M) | Sell (M)
    """

    # --- Load raw CSV ---
    df = pd.read_csv(input_path, header=None)

    # --- Identify the header rows ---
    # Row 0: Junk index row  (0, 1, 2, 3...)
    # Row 1: Demographic row (Trade, Egyptians, Egyptians, Arabs, Arabs, Foreigners, Foreigners, Totals, Totals)
    # Row 2: Type row        (Trade, Ret., Inst., Ret., Inst., Ret., Inst., Ret., Inst.)
    # Rows 3+: Data rows     (Timestamp, Metric_Name, val1, val2, ...)

    # Find the two header rows by looking for "Egyptians" in the row
    demo_row_idx = df[df.apply(lambda r: r.astype(str).str.contains('Egyptians').any(), axis=1)].index[0]
    type_row_idx = demo_row_idx + 1

    demographics  = df.iloc[demo_row_idx, 2:8].tolist()   # cols 2-7: exclude Totals
    investor_types = df.iloc[type_row_idx, 2:8].tolist()  # cols 2-7

    # --- Filter only Buy and Sell data rows (exclude pre-calculated rows) ---
    data_df = df[df.iloc[:, 1].isin(['Buy (M)', 'Sell (M)'])].copy()

    records = []

    for timestamp in data_df.iloc[:, 0].unique():
        ts_data = data_df[data_df.iloc[:, 0] == timestamp]

        buy_row  = ts_data[ts_data.iloc[:, 1] == 'Buy (M)']
        sell_row = ts_data[ts_data.iloc[:, 1] == 'Sell (M)']

        if buy_row.empty or sell_row.empty:
            continue

        buy_vals  = buy_row.iloc[0, 2:8].tolist()
        sell_vals = sell_row.iloc[0, 2:8].tolist()

        for i in range(len(demographics)):
            try:
                buy_val  = float(str(buy_vals[i]).replace(',', ''))
                sell_val = float(str(sell_vals[i]).replace(',', ''))
            except (ValueError, TypeError):
                continue  # skip if value is not a valid number

            records.append({
                'Timestamp':     timestamp,
                'Demographic':   demographics[i],
                'Investor_Type': investor_types[i],
                'Buy (M)':       buy_val,
                'Sell (M)':      sell_val,
            })

    result_df = pd.DataFrame(records)

    # --- Derive calculated columns so Power BI doesn't need DAX for basics ---
    result_df['Net (M)']      = result_df['Buy (M)'] - result_df['Sell (M)']
    result_df['Turnover (M)'] = result_df['Buy (M)'] + result_df['Sell (M)']

    result_df.to_csv(output_path, index=False, encoding='utf-8-sig')
    print(f"Clean file saved to: {output_path}")
    print(f"Total rows: {len(result_df)}")
    print()
    print(result_df.to_string(index=False))
    return result_df


if __name__ == "__main__":
    transform_institutional_data(
        input_path=r'c:\Users\drago\Desktop\EFG\Task 2\institutional_foreign_data.csv',
        output_path=r'c:\Users\drago\Desktop\EFG\Task 2\institutional_foreign_clean.csv'
    )

import requests
import pandas as pd
from bs4 import BeautifulSoup
import urllib.request
import time
import os
from datetime import datetime

# ---------- Paths ----------
RAW_INST_PATH   = 'institutional_foreign_data.csv'
CLEAN_INST_PATH = 'institutional_foreign_clean.csv'
BLOCK_PATH      = 'block_trades.csv'


# ---------- Transform helper ----------
def transform_institutional_data():
    """
    Reads the raw institutional_foreign_data.csv (messy multi-header format)
    and writes a clean, flat Power BI-ready CSV to institutional_foreign_clean.csv.
    The clean file is always fully regenerated (never appended) so it stays
    consistent with the full history in the raw file.
    """
    if not os.path.exists(RAW_INST_PATH):
        print("[Transform] Raw file not found, skipping transform.")
        return

    df = pd.read_csv(RAW_INST_PATH, header=None)

    # Find the demographic header row (contains 'Egyptians')
    demo_row_idx = df[df.apply(
        lambda r: r.astype(str).str.contains('Egyptians').any(), axis=1
    )].index[0]
    type_row_idx = demo_row_idx + 1

    demographics   = df.iloc[demo_row_idx, 2:8].tolist()  # exclude Totals cols
    investor_types = df.iloc[type_row_idx,  2:8].tolist()

    # Keep only Buy and Sell rows (discard pre-calculated Net, Turnover, etc.)
    data_df = df[df.iloc[:, 1].isin(['Buy (M)', 'Sell (M)'])].copy()

    records = []
    for timestamp in data_df.iloc[:, 0].unique():
        ts = data_df[data_df.iloc[:, 0] == timestamp]
        buy_row  = ts[ts.iloc[:, 1] == 'Buy (M)']
        sell_row = ts[ts.iloc[:, 1] == 'Sell (M)']

        if buy_row.empty or sell_row.empty:
            continue

        buy_vals  = buy_row.iloc[0,  2:8].tolist()
        sell_vals = sell_row.iloc[0, 2:8].tolist()

        for i in range(len(demographics)):
            try:
                b = float(str(buy_vals[i]).replace(',', ''))
                s = float(str(sell_vals[i]).replace(',', ''))
            except (ValueError, TypeError):
                continue

            records.append({
                'Timestamp':     timestamp,
                'Demographic':   demographics[i],
                'Investor_Type': investor_types[i],
                'Buy (M)':       b,
                'Sell (M)':      s,
                'Net (M)':       round(b - s, 2),
                'Turnover (M)':  round(b + s, 2),
            })

    result_df = pd.DataFrame(records)
    # Overwrite (not append) — always reflects full history from the raw file
    result_df.to_csv(CLEAN_INST_PATH, index=False, encoding='utf-8-sig')
    print(f"[Transform] Clean file updated → {len(result_df)} rows saved to {CLEAN_INST_PATH}")

def scrape_and_append():
    url = 'https://www.sigma-cap.com/main/fl_market_page.overview?u_sess='
    
    # 1. Fetch the page
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read()
    except Exception as e:
        print(f"Failed to fetch: {e}")
        return

    soup = BeautifulSoup(html, 'html.parser', from_encoding='windows-1256')
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 2. Scrape Institutional / Foreign
    tables = soup.find_all('table', class_='marginTable')
    inst_foreign_table = next((t for t in tables if 'Egyptians' in t.text and 'Foreigners' in t.text), None)
    
    if inst_foreign_table:
        try:
            from io import StringIO
            df_inst = pd.read_html(StringIO(str(inst_foreign_table)))[0]
        except Exception:
            df_inst = pd.read_html(str(inst_foreign_table))[0]
            
        if isinstance(df_inst.columns, pd.MultiIndex):
            df_inst.columns = ['_'.join(col).strip() for col in df_inst.columns.values]
            
        # Add a timestamp column so we know when this data was fetched
        df_inst.insert(0, 'Timestamp', current_time)
        
        # Save to CSV (append mode)
        file_exists = os.path.exists(RAW_INST_PATH)
        df_inst.to_csv(RAW_INST_PATH, mode='a', index=False, header=not file_exists, encoding='utf-8-sig')
        print(f"[{current_time}] Appended Institutional data.")

    # 3. Scrape Block Trades
    block_trades_table = next((t for t in soup.find_all('table') if 'Share Name' in t.text and 'Value EGP' in t.text), None)
    
    if block_trades_table:
        try:
            from io import StringIO
            df_block = pd.read_html(StringIO(str(block_trades_table)))[0]
        except Exception:
            df_block = pd.read_html(str(block_trades_table))[0]
            
        if df_block.iloc[0].astype(str).str.contains('Share Name').any():
            df_block.columns = df_block.iloc[0]
            df_block = df_block[1:].reset_index(drop=True)
            
        if str(df_block.columns[0]).startswith('Unnamed') or pd.isna(df_block.columns[0]) or str(df_block.columns[0]).strip() == '':
            df_block = df_block.drop(df_block.columns[0], axis=1)
            
        # Add a timestamp column
        df_block.insert(0, 'Timestamp', current_time)
        
        # Save to CSV (append mode)
        file_exists = os.path.exists(BLOCK_PATH)
        df_block.to_csv(BLOCK_PATH, mode='a', index=False, header=not file_exists, encoding='utf-8-sig')
        print(f"[{current_time}] Appended Block Trades data.")

if __name__ == "__main__":
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Starting single scrape execution...")
    scrape_and_append()
    transform_institutional_data()   # Auto-regenerate clean CSV after every scrape
    print("Finished execution.")

# EFG ONE Synthetic CSV Dataset

This dataset contains raw, app-supported columns only. Calculated fields were intentionally excluded so they can be created in Power BI using DAX measures or calculated columns.

## CSV Files

- `users.csv`: anonymous customers with segment, country, risk profile, and registration date.
- `login_sessions.csv`: raw login sessions with device, OS, app version, and session duration.
- `app_events.csv`: raw screen and feature events for engagement analytics.
- `stocks.csv`: stock reference data.
- `funds.csv`: mutual fund reference and fact sheet fields.
- `market_calendar.csv`: EGX market open/closed status by date.
- `market_indices.csv`: EGX30 and EGX70 index values.
- `market_trades.csv`: executed market trades. Use this to derive stock price movement, volume, turnover, OHLC, VWAP, top gainers, top losers, and highest turnover.
- `order_book_snapshots.csv`: bid/ask market depth.
- `stock_recommendations.csv`: top picks with buy guidance, stop loss, and targets.
- `featured_lists.csv`: intraday, OTC, and most liked stock lists.
- `watchlists.csv`: user watchlist membership.
- `stock_orders.csv`: user stock orders.
- `stock_transactions.csv`: completed stock buy/sell transactions.
- `cash_transactions.csv`: wallet deposits and withdrawals.
- `fund_daily_prices.csv`: mutual fund certificate prices over time.
- `fund_orders.csv`: mutual fund invest/redeem orders.

## Measures To Create In Power BI

### Customer Analytics

- Total customers = distinct count of user IDs.
- Active customers = distinct users with at least one session or event in the selected period.
- New customers = count of users by registration date.
- New customer acquisition = new customers by selected period.
- Customer growth = new customers over time.
- Customer growth rate = current period new customers compared with previous period.
- Retention rate = users active in a later period / users active or registered in an earlier period.
- Segmentation = customers grouped by client segment or risk profile.
- Geographic distribution = customers grouped by country.

### Digital Adoption

- DAU = distinct users with sessions/events per day.
- MAU = distinct users with sessions/events per month.
- Login frequency = count of sessions per user or average sessions per active user.
- Average session duration = average session duration seconds.
- Most visited screens = count of events grouped by screen name.
- Feature utilization = distinct users or event count by feature name.
- Feature adoption rate = users using a feature / total active users.
- App engagement score = weighted score using sessions, events, active days, and feature usage.

### Trading Analytics

- Stock turnover = trade price x quantity.
- Daily trading volume = sum of trade quantity.
- Trading volume = sum of trade quantity.
- Trading value = sum of stock turnover.
- Number of trades = count of trade IDs.
- Orders count = count of stock order IDs and fund order IDs.
- Buy orders count = count of buy/invest orders.
- Sell orders count = count of sell/redeem orders.
- Buy vs sell analysis = compare buy/invest order count or value against sell/redeem order count or value.
- Open price = first trade price in the selected period.
- High price = max trade price in the selected period.
- Low price = min trade price in the selected period.
- Close price = last trade price in the selected period.
- Previous close = prior period close.
- Stock change = close price - previous close.
- Stock change % = stock change / previous close.
- VWAP = sum(price x quantity) / sum(quantity).
- Top gainers and losers = rank by stock change %.
- Highest turnover = rank by turnover.
- Top traded securities = rank stocks by trading value, trading volume, or number of trades.
- Market breadth = count gainers, losers, and unchanged stocks.
- Market activity = number of trades, trading volume, trading value, active stocks, and market status.

### Portfolio Analytics

- Order value = order price x quantity.
- Transaction value = transaction price x quantity.
- Portfolio quantity = buys minus sells.
- Portfolio market value = holding quantity x latest price.
- Unrealized P/L = market value - total cost.
- Cash balance = approved deposits - approved withdrawals.
- Total wealth = cash balance + portfolio market value.
- Portfolio allocation % = asset value / total portfolio value.
- Asset allocation = portfolio market value grouped by asset type.
- Portfolio distribution = customers or value grouped by portfolio size band, asset type, or risk profile.
- Daily P/L = current portfolio value - previous day portfolio value.
- AUM = total portfolio market value across all customers.
- AUM trends = AUM by date.
- Average portfolio value = AUM / number of customers with portfolio value.

### Executive Dashboard KPIs

- Active users = distinct active users in selected period.
- Trading value = sum of stock turnover.
- AUM = total portfolio market value across all customers.
- New customer acquisition = new customers by selected period.
- Key business KPIs = active users, trading value, AUM, new customers, orders count, and retention rate.

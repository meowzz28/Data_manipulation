import pandas as pd

df = pd.read_csv('companies_pricing_data.csv')

#Q1
df['PRICEMID'] = (df['PRICEHIGH'] + df['PRICELOW']) / 2

#Q2 
df['SMA_5'] = df.groupby('TICKER')['PRICECLOSE'].transform(lambda x: x.rolling(window=5).mean())

#Q3 
df['DAILY_RETURN'] = df.groupby('TICKER')['PRICECLOSE'].transform(lambda x: x.pct_change() * 100)

#Q4
df['DATE'] = pd.to_datetime(df['DATE'], format='%d/%m/%y')
df = df.set_index('DATE')
df = df.groupby('TICKER').apply(lambda group: group.asfreq('D', method='pad')).reset_index(level=0, drop=True)
df['MONTHLY_RETURN'] = df.groupby('TICKER')['PRICECLOSE'].transform(lambda x: x.pct_change(periods=30) * 100)
df = df.reset_index()

original_df = pd.read_csv('companies_pricing_data.csv')
original_df['DATE'] = pd.to_datetime(original_df['DATE'], format='%d/%m/%y')

df = pd.merge(df, original_df[['DATE', 'TICKER']], on=['DATE', 'TICKER'], how='inner')

print(df[:31])
df.to_csv('e1375499.csv', sep=',')
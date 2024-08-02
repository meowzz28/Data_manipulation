import pandas as pd
#Q6
df = pd.read_csv('Modified_csv.csv')

std_price_close = df['PRICECLOSE'].std()

std_price_close_rounded = round(std_price_close)

print(f"STD: {std_price_close_rounded}")
#Q7
min_price_low = df['PRICELOW'].min()

min_price_low_rounded = round(min_price_low, 2)

print(f"MIN_PRICE_LOW:{min_price_low_rounded}")
#Q8
start_date = '2021-01-01'
end_date = '2021-06-30'
mask = (df['DATE'] >= start_date) & (df['DATE'] <= end_date)
df_filtered = df[mask]
df_financials = df_filtered[df_filtered['SECTOR'] == 'Financials']

lowest_return_row = df_financials.loc[df_financials['DAILY_RETURN'] == df_financials['DAILY_RETURN'].min()]
print(lowest_return_row)

#Q9
it_sector = df[df['SECTOR'] == 'Information Technology']
highest_monthly_return_row = it_sector.loc[it_sector['MONTHLY_RETURN'] == it_sector['MONTHLY_RETURN'].max()]
print(highest_monthly_return_row)

#Q10
start_date = '2021-01-01'
end_date = '2021-12-31'
mask = (df['DATE'] >= start_date) & (df['DATE'] <= end_date)
df_filtered = df[mask]
sector_avg_monthly_return = df_filtered.groupby('SECTOR')['MONTHLY_RETURN'].mean()
print(sector_avg_monthly_return)
print(sector_avg_monthly_return.max())

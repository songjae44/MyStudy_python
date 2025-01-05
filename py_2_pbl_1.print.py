from py_2_pbl_1 import SalesAnalysis as sa

x = sa(2024)
print(type(x.year))

dates = x.create_dates()
print(dates)

sales = x.create_sales()
print(sales)

df = x.data_to_df()
print(df)

monthly_sale = x.monthly_sale()
print(monthly_sale)

graph = x.plot_grapgh()
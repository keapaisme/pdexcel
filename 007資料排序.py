import pandas as pd

products = pd.read_excel('./temp/List.xlsx', index_col='ID')

products.sort_values(by=['Price', 'Name'], inplace=True, ascending=[False, False])

print(products)

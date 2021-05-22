# -*- codeing = utf-8 -*-
# @Time :2021/5/13 21:18
# @Author: Kas Huang
# @File:001.py.py
# @Software:PyCharm

import pandas as pd

'''
df = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Tim', 'Victor', 'Nick'], '數學': [67, 88, 79], '生物': [87, 98, 89]})
df = df.set_index('ID')
df.to_excel('c:/users/kas/desktop/pdlab/019.xlsx')

print(df)
print(df.sum(), df.mean())
'''

df = pd.read_excel('c:/users/kas/desktop/pdlab/019.xlsx', index_col='ID')

temp = df[['數學', '生物']]
row_sum = temp.sum(axis=1)
row_mean = temp.mean(axis=1)
df['sum'] = row_sum
df['mean'] = row_mean

col_mean = df[['數學', '生物', 'sum', 'mean']].mean()
col_mean['Name']='summary'
df = df.append(col_mean, ignore_index=True)


print(df)
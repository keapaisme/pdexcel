# -*- codeing = utf-8 -*-
# @Time :2021/5/22 12:27
# @Author: Kas Huang
# @File:023pilot數據透視表.py
# @Software:PyCharm

import pandas as pd
import numpy as np

pd.options.display.max_columns=999
pp = pd.read_excel('temp\Orders.xlsx')
# print(pp.head())
# print(pp.Date.dtype)  # 確認'Date' 欄是否是Date類還是是series類 print(pp.Total.dtype)

'''
pp['Year'] = pd.DatetimeIndex(pp['Date']).year
pt1 = pp.pivot_table(index='Category', columns='Year', values='Total', aggfunc=np.sum)  # aggfunc(聚合函數)
print(pt1)
'''  # 方法一,調用Pandas裡的PIVOT_TABLE

# 方法二,自行寫
pp['Year'] = pd.DatetimeIndex(pp['Date']).year

groups = pp.groupby(['Category', 'Year'])
s = groups['Total'].sum() / 10000
c = groups['ID'].count()

pt2 = pd.DataFrame({'Sum': s, 'Count': c})
print(pt2)

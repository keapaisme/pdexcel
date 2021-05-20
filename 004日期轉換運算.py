# -*- codeing = utf-8 -*-
# @Time :2021/5/13 22:12
# @Author: Kas Huang
# @File:004.py
# @Software:PyCharm
# df.to_excel('c:/users/kas/desktop/pdlab/001.xlsx')

import pandas as pd
from datetime import date, timedelta


def add_month(d, md):
    yd = md // 12
    m = d.month + md % 12
    if m != 12:
        yd += m // 12
        m = m % 12
    return date(d.year + yd, m, d.day)


start = date(2021, 5, 13)
books = pd.read_excel('c:/users/kas/desktop/pdlab/books.xlsx', skiprows=3, usecols="c:f", dtype={'ID': str, 'InStore': str, 'Date': str})  # 跳過三行讀C:F列

'''
for i in books.index:
    books['ID'].at[i] = i + 1
    books['InStore'].at[i] = 'Yes' if i%2 == 0 else 'No'
    # books['Date'].at[i] = start + timedelta(days=i)  # 日遞增,用timedelta 最大單位為 DAYS
    # books['Date'].at[i] = date(start.year+i, start.month, start.day)  # 月分遞增
    books['Date'].at[i] = add_month(start, i)
'''  # 調出整个序列改值

# 直接針對表格的CELL改值 用 datafram
for i in books.index:
    books.at[i, 'ID'] = i + 1
    books.at[i, 'InStore'] = 'Yes' if i % 2 == 0 else 'No'
    # books['Date'].at[i] = start + timedelta(days=i)  # 日遞增,用timedelta 最大單位為 DAYS
    # books['Date'].at[i] = date(start.year+i, start.month, start.day)  # 月分遞增
    books.at[i, 'Date'] = add_month(start, i)

books.set_index('ID', inplace=True)
print(books)
books.to_excel('c:/users/kas/desktop/pdlab/Output.xlsx')
'''
s1 = pd.Series([1, 2, 3], index=[1, 2, 3], name='A')
s2 = pd.Series([10, 20, 30], index=[1, 2, 3], name='B')
s3 = pd.Series([100, 200, 300], index=[2, 3, 4], name='C')

df = pd.DataFrame({s1.name: s1, s2.name: s2, s3.name: s3})  # 以字典形式
# df2 = pd.DataFrame([s1, s2, s3])  # 以列表形式加入數列
print(df)
'''


'''
l1 = [100, 200, 300]
l2 = ['x', 'y', 'z']

s1 = pd.Series(l1, index=l2)
s2 = pd.Series([12, 13, 14], index=['k', 'a', 's'])
print(s1)
print(s2)
'''

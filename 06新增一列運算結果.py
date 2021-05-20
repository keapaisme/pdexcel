# -*- codeing = utf-8 -*-
# @Time :2021/5/13 22:12
# @Author: Kas Huang
# @File:004.py
# @Software:PyCharm
# df.to_excel('c:/users/kas/desktop/pdlab/001.xlsx')

import pandas as pd
import os

from datetime import date, timedelta

books = pd.read_excel('./temp/Books.xlsx', index_col='ID')
s1 = ['stock']
print(books.columns)
books.insert(books.shape[1], 'Stock', 0)
books.insert(books.shape[1], 'Type', 0)
books['Type'] = books['Type'].apply(lambda x: x + 2)



for i in range(1, 4):
    books['Price'].at[i] = 28
print(books)

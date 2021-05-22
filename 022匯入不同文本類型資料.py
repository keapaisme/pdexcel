# -*- codeing = utf-8 -*-
# @Time :2021/5/22 12:12
# @Author: Kas Huang
# @File:022匯入不同文本類型資料.py
# @Software:PyCharm

import pandas as pd

db = pd.read_csv('temp\Students.csv', sep=',', index_col='ID')  # .csv 以,分隔
print(db)

db1 = pd.read_csv('temp\Students.tsv', sep='\t', index_col='ID')  # .tsv 以TAB (\t)分隔
print(db1)

db3 = pd.read_csv('temp\Students.txt', sep='|', index_col='ID')  # .txt 以|分隔
print(db3)
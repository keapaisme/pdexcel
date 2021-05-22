# -*- codeing = utf-8 -*-
# @Time :2021/5/22 11:02
# @Author: Kas Huang
# @File:020刪附多餘資料.py
# @Software:PyCharm

import pandas as pd

pd.options.display.max_columns=40
db = pd.read_excel('temp\Students_Duplicates.xlsx', index_col='Name')

table = db.transpose()
print(table)
# print(dup.any())
# db.drop_duplicates(subset='Name', inplace=True, keep='last')


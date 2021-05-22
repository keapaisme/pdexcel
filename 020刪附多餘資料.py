# -*- codeing = utf-8 -*-
# @Time :2021/5/22 11:02
# @Author: Kas Huang
# @File:020刪附多餘資料.py
# @Software:PyCharm

import pandas as pd

db = pd.read_excel('temp\Students_Duplicates.xlsx')
dupe = db.duplicated(subset='Name')
dupe = dupe[dupe == True]  # dupe = dupe[dupe]
print(dupe.index)
print(db.iloc[dupe.index])
# print(dup.any())
# db.drop_duplicates(subset='Name', inplace=True, keep='last')


# -*- codeing = utf-8 -*-
# @Time :2021/5/13 21:41
# @Author: Kas Huang
# @File:002.py
# @Software:PyCharm

import pandas as pd
people = pd.read_excel('c:/users/kas/desktop/pdlab/people.xlsx', index_col='ID')  # ,head=1 設定第一列為欄位名稱 ,index_col='ID' 將ID欄指定為INDEX

# people = pd.read_excel('c:/users/kas/desktop/pdlab/people.xlsx', header= None)  # 不要設定欄位名,自己動手添加 columns
# people.columns = ['ID', 'Type', 'Title', 'FirstName', 'MiddleName', 'LastName']
# print(people.shape)  # 總筆數, 總欄數
print(people.columns)  # 欄位名稱及屬性
print(people.head(3))
# print(people.tail(3))



# -*- codeing = utf-8 -*-
# @Time :2021/5/19 12:37
# @Author: Kas Huang
# @File:017.py
# @Software:PyCharm

import pandas as pd

db = pd.read_excel('temp/books.xlsx')
sp = db['Name'].str.split('_', expand=True)
db['A'] = sp[0]
db['B'] = sp[1]
print(db)

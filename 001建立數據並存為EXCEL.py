# -*- codeing = utf-8 -*-
# @Time :2021/5/13 21:18
# @Author: Kas Huang
# @File:001.py.py
# @Software:PyCharm

import pandas as pd

df = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Tim', 'Victor', 'Nick']})
df = df.set_index('ID')
df.to_excel('c:/users/kas/desktop/pdlab/001.xlsx')

print(df)

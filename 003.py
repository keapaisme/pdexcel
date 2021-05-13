# -*- codeing = utf-8 -*-
# @Time :2021/5/13 22:12
# @Author: Kas Huang
# @File:003.py
# @Software:PyCharm

import pandas as pd

s1 = pd.Series([1, 2, 3], index=[1, 2, 3], name='A')
s2 = pd.Series([10, 20, 30], index=[1, 2, 3], name='B')
s3 = pd.Series([100, 200, 300], index=[2, 3, 4], name='C')

df = pd.DataFrame({s1.name: s1, s2.name: s2, s3.name: s3})  # 以字典形式
# df2 = pd.DataFrame([s1, s2, s3])  # 以列表形式加入數列
print(df)



'''
l1 = [100, 200, 300]
l2 = ['x', 'y', 'z']

s1 = pd.Series(l1, index=l2)
s2 = pd.Series([12, 13, 14], index=['k', 'a', 's'])
print(s1)
print(s2)
'''

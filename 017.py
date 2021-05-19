# -*- codeing = utf-8 -*-
# @Time :2021/5/19 12:37
# @Author: Kas Huang
# @File:017.py
# @Software:PyCharm

import pandas as pd

'''
def score_validation(row):
    try:
        assert 0<= row.Score <= 100
    except:
        print(f'#{row.ID}\t學生: {row.Name} 分數為{row.Score} 是錯誤')
'''  # score_validation() 以TRY EXCEPT 做驗証

def score_validation(row):
    if not 0 <=row.Score<= 100:
        print(f'#ID {row.ID} \t 學生:{row.Name} 的分數:{row.Score} 是錯的')
# score_validation() 以 if not 做驗証

students = pd.read_excel('temp/17Students.xlsx')
# print(students)
students.apply(score_validation, axis=1)
import pandas as pd

idlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
c1list = ['Kas', 'Tide', 'Joy', 'Benz', 'Eagle', 'Bob', 'Lee', 'Alex', 'Tim', 'Hedy', 'Judy', 'Ada', 'Mary', 'Kevin']
c2list = [78, 69, 97, 49, 87, 20, 45, 78, 100, 66, 59, 92, 85, 79]
c3list = [52, 51, 19, 15, 15, 26, 31, 28, 36, 45, 32, 25, 29, 21]


def validate_age(a):
    return 10 <= a <= 52

def level_b(s):
    return 60 <= s < 100


c1 = pd.Series(c1list, index=idlist, name="student")
c2 = pd.Series(c2list, index=idlist, name='score')
c3 = pd.Series(c3list, index=idlist, name='AGE')
students = pd.DataFrame({c1.name: c1, c2.name: c2, c3.name: c3})

# students =students.loc[students['score'].apply(level_b)]
students.to_excel('temp/Students.xlsx')
print(students)
'''
students = pd.read_excel('temp/Students.xlsx', index_col=0)
print(students, end='\n'*3)
alist = students.loc[students['AGE'].apply(validate_age)].loc[students['score'].apply(level_b)]
print('1:', alist, end='\n'*3)
blist = students.loc[students.AGE.apply(validate_age)].loc[students.score.apply(level_b)]
print('2:', blist, end='\n'*3)
clist = students.loc[students.AGE.apply(lambda a: 34 <= a <= 55)]. \
    loc[students.score.apply(lambda s: 10 <= s <= 100)]  # " ＂＋ ＼ 程式太長斷行
print('3:', clist)
'''
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


font = FontProperties(fname=r"C:\Windows\Fonts\STHUPO.TTF", size=14)
students = pd.read_excel('temp/Students.xlsx')
# print(students)
students.sort_values(by='score', inplace=True, ascending=False)
# students.plot.bar(x='student', y='score', color='red', title='2nd Exam Score')
plt.bar(students.student, students.score, width=0.5)
plt.xticks(students.student, rotation='90')

plt.title('期中考成绩', FontProperties=font)
plt.xlabel('姓名', FontProperties=font)
plt.ylabel('分数', FontProperties=font)
plt.tight_layout()
plt.show()

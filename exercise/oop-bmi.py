"""
試以物件導向的方式打造出程式設計班學生資料集

變數(屬性)包含以下內容

學生人數
學生班級

姓名
座號
身高
體重

學生班級及學生人數請以類別變數來設定。

請產生出至少5位同學的資料(物件)並設定好以上的物件變數。
請呼叫以下函數
(1)類別函數-->計算BMI值。
(2)類別函數-->印出BMI值並給建議。
"""

import math


class StudentInfo(object):
    students = 0
    className = "Unknown"

    def __init__(self, name, seat, hight, weight):
        self.name = name
        self.seat = seat
        self.height = hight
        self.weight = weight
        StudentInfo.students += 1

    def calcualteBMI(self):
        if self.height > 10:
            height = self.height / 100
        else:
            height = self.height
        return self.weight / math.pow(height, 2)

    def getStudentsCount():
        return StudentInfo.students

    def __str__(self):
        return f"BMI of ({self.seat:02}) {self.name} = {self.calcualteBMI():05.2f}."


if __name__ == "__main__":
    StudentInfo.className = "Python + AI"
    students = ["Albert", "Bob", "Clare", "David", "Ember"]
    seatNo = 5
    height = 165
    weight = 65
    for i, name in enumerate(students):
        students[i] = StudentInfo(name, seatNo, height, weight)
        seatNo += 5
        height += 5
        weight += 5

    print(
        f"There are {StudentInfo.getStudentsCount():02} students in the [{StudentInfo.className}] class."
    )
    print("=" * 50)
    for student in students:
        print(student)

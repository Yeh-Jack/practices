# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


# %%
class Animal:
    def __init__(self, spicy):  # 建構函式或初始化函式
        self.spicy = spicy  # 實例屬性，實例變數  --> 物件屬性，物件變數


# %%
class Employee(Animal):
    "Common base class for all employees"

    empCount = 0  # 類別變數 ， 類別屬性

    def __init__(self, name, salary):  # 建構函式或初始化函式
        self.name = name  # 實例屬性，實例變數  --> 物件屬性，物件變數
        self.salary = salary  # 實例屬性，實例變數  --> 物件屬性，物件變數
        Employee.empCount += 1

    def displayCount(self):  # 類別內的一般函式
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):  # 類別內的一般函式
        print("Name : ", self.name, ", Salary: ", self.salary)


print("Employee.__bases__:", Employee.__bases__)

## This would create first object of Employee class
emp1 = Employee(
    "Maxsu", 2000
)  # 呼叫Employee初始化函式  --> 呼叫帶有二個參數的初始化函式
## This would create second object of Employee class
emp2 = Employee(
    "Kobe", 5000
)  # 呼叫Employee初始化函式  --> 呼叫帶有二個參數的初始化函式

emp3 = Employee("louis", 15000)

emp1.displayEmployee()  # 物件emp1呼叫displayEmployee()函式
emp2.displayEmployee()  # 物件emp2呼叫displayEmployee()函式
emp3.displayEmployee()  # 物件emp3呼叫displayEmployee()函式

print("Total Employee %d" % Employee.empCount)  # 存取類別變數


emp1.displayCount()
emp2.displayCount()
emp3.displayCount()


emp1.salary = 6000  # Modify an 'salary' attribute.
emp1.name = "sony"  # Modify 'name' attribute.
del emp1.salary  # Delete 'salary' attribute.

print(emp1.name)  # 存取emp1.name變數(屬性)
# print(emp1.salary)   #存取emp1.salary變數(屬性)

emp1.salary = 10000  # Modify an 'salary' attribute.
print(emp1.name)  # 存取emp1.name變數(屬性)
print(emp1.salary)  # 存取emp1.salary變數(屬性)

emp1.displayEmployee()
# print ("Employee.__doc__:", Employee.__doc__)


print(hasattr(emp1, "salary"))  # Returns true if 'salary' attribute exists
emp_salary = getattr(
    emp1, "salary"
)  # 等同於emp1.salary     # Returns value of 'salary' attribute
print("emp1_salary is:", emp_salary)

delattr(emp1, "salary")  # 等同於del emp1.salary


# %%
class Student(Employee):
    "Common base class for all students"

    stuCount = 0

    def __init__(self, name, stuid):
        self.name = name
        self.stuid = stuid
        Student.stuCount += 1

    def displayCount(self):
        "Displays totoal students count."
        print("Total Student %d" % Student.stuCount)

    def displayStudent(self):
        print("Name : ", self.name, ", stuid: ", self.stuid)


stu1 = Student("Apple", "A01")
stu2 = Student("sony", "A02")

stu1.displayStudent()
stu2.displayStudent()

stu1.displayCount()


print("Student.__doc__:", Student.__doc__)
print("Student.__name__:", Student.__name__)
print("Student.__module__:", Student.__module__)
print("Student.__bases__:", Student.__bases__)
print("Student.__dict__:", Student.__dict__)

print("Student.displayCount.__doc__:", Student.displayCount.__doc__)


# %%
# ## This would create first object of Employee class
# emp1 = Employee("Maxsu", 2000)
# ## This would create second object of Employee class
# emp2 = Employee("Kobe", 5000)

# emp3 = Employee("louis", 15000)

# emp1.displayEmployee()
# emp2.displayEmployee()
# emp3.displayEmployee()
# print("Total Employee %d" % Employee.empCount)


# emp1.salary = 6000  # Modify an 'salary' attribute.
# emp1.name = 'xyz'  # Modify 'name' attribute.
# # del emp1.salary  # Delete 'salary' attribute.

# print(emp1.name)
# print(emp1.salary)


# print(hasattr(emp1, 'salary'))         # Returns true if 'salary' attribute exists
# emp_salary=getattr(emp1, 'salary')         # Returns value of 'salary' attribute
# print("emp1_salary is:",emp_salary)

# setattr(emp1, 'salary', 7000)   # Set attribute 'salary' at 7000
# delattr(emp1, 'salary')         # Delete attribute 'salary'
# # print(emp1.salary)

# print ("Student.__doc__:", Student.__doc__)
# print ("Student.__name__:", Student.__name__)
# print ("Student.__module__:", Student.__module__)
# print ("Student.__bases__:", Student.__bases__)
# print ("Student.__dict__:", Student.__dict__ )

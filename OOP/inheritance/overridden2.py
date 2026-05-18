# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
 1+2
 1*2
 1/2
 'abc'+'cde'
 '123'+564
 
 
 obj1+obj2

 
 
 class louis():
     def __str__(self):
         print()
     pass
 
    obj3=louis()
    
    obj3+obj4
 
 print(obj3)


"""


class Vector:
    def __init__(self, a, b):
        self.a = a  # v1.a=2
        self.b = b  # v1.b=10

    def __str__(self):
        return "Vector_value =  (%d, %d)" % (self.a, self.b)

    def __add__(self, p2):
        return Vector(self.a + p2.a, self.b + p2.b)

    def __sub__(self, p2):
        return Vector(self.a - p2.a, self.b - p2.b)


v1 = Vector(2, 10)
print("v1 value = ")
print(v1)
print()

v2 = Vector(5, -2)
print("v1.__add__(v2) = ")
print(v1 + v2)  # v1.__add__(v2)
print()

print("v1.__sub__(v2) = ")
print(v1 - v2)  # v1.__sub__(v2)

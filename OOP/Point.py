# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import time

class Point:
   def __init__(self, x=0, y=0):
      self.x = x
      self.y = y
      
   def __del__(self):
      class_name = self.__class__.__name__
      print (class_name, "destroyed")
      
         

pt1 = Point()

pt11 = Point()

pt2 = pt1
pt3 = pt1


print (id(pt1));   # prints the ids of the obejcts


del pt1

print(pt2.x)

print(pt2.y)

del pt2

# print(pt2.x)

# print(pt2.y)

del pt3  # 因為沒有物件去指向Point所打造出來的物件  --＞　就會去呼叫__del__


time.sleep(30)

pt4 = Point()

print (id(pt4))


del pt4

print(id(pt11))
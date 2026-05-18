# -*- coding: utf-8 -*-
"""
Created on Mon May 31 08:29:47 2021

@author: Alvin
"""
class MyClass1(object):
   def setAge(self, num):
      self.__age = num

   def getAge(self):
      return self.__age



class MyClass(object):
   def setAge(self, num):
      self.age = num

   def getAge(self):
      return self.age

## 範例化物件
zack = MyClass()
zack.setAge(45)
print(zack.getAge())
zack.setAge("Fourty Five")
print(zack.getAge())

zack.age=28
print(zack.age)

## 範例化物件  私有屬性(Private Attribute)

apple = MyClass1()
apple.setAge(45)
print(apple.getAge())
apple.setAge("Fourty Five")
print(apple.getAge())


apple.__age=28
print(apple.__age)
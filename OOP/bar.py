# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 06:32:24 2021

@author: Alvin
"""

import foo

#等同於載入這些內容
#foo.py


print(__name__)       # 輸出：_ _main_ _
print(foo.__name__)   # 輸出：foo


foo.foo_print()

foo.foo_louis()

print(foo.alex)

print(foo.alvin)

print(foo.eric)


myclass_obj1=foo.MyClass()

myclass_obj1.showInfo()


#%%

from foo import *  #載入foo模組裡的所有功能(foo_print(),foo_louis())

#等同於載入這些內容
# class MyClass():
#     def __init__(self, a="hello", b="world"):     # 設定參數之預設值
#         self._a=a              # 被保護的屬性
#         self.__b=b             # 私有的屬性
    
#     def showInfo(self):
#         print("a =", self._a, "b =", self.__b)    # 透過 self 物件存取其屬性

# def foo_print() : 
#     print("lccnet" )
# 	
# def foo_louis() : 
#     print("louis" )
    
# alex="ok"
# eric="good"
# alvin="nice"
    
# print("foo:" , __name__ )


foo_print()
foo_louis()

print(alex)
print(eric)
print(alvin)



myclass_obj2=MyClass("louis","lccnet")

myclass_obj2.showInfo()


#%%

from foo import alex,eric,alvin,foo_louis,foo_print
# from matplotlib import plotly

#等同於載入這些內容
# def foo_print() : 
#     print("lccnet" )
# 	
# def foo_louis() : 
#     print("louis" )
    
# alex="ok"
# eric="good"
# alvin="nice"


foo_print()
foo_louis()

print(alex)
print(eric)
print(alvin)


























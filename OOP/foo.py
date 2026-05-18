# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 06:40:18 2021

@author: Alvin
"""

class MyClass():
    def __init__(self, a="hello", b="world"):     # 設定參數之預設值
        self._a=a              # 被保護的屬性
        self.__b=b             # 私有的屬性
    
    def showInfo(self):
        print("a =", self._a, "b =", self.__b)    # 透過 self 物件存取其屬性

def foo_print() : 
    print("lccnet" )
	
def foo_louis() : 
    print("louis" )
    
alex="ok"
eric="good"
alvin="nice"
    

print("foo:" , __name__ )

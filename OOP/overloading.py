# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class Human:  
   def sayHello(self, name = None , value=None):    # @overloading
      if name is not None:
         print('Hello ' + name)
      else:
         print('Hello ')

#Create Instance  # 建構物件obj  --> 用Human類別來建構
obj = Human()

#Call the method, else part will be executed
obj.sayHello()  # Hello

#Call the method with a parameter, if part will be executed
obj.sayHello(name='Rahul')  # Hello Rahul


obj.sayHello(name='lccnet',value=100)
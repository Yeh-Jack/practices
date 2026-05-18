# -*- coding: utf-8 -*-
"""
Created on Fri Dec  5 19:58:06 2025

@author: USER
"""

def my_func():
    print("my_func content")
    
    
def second_func():
    print("second_func content")
    
def another_func(func):
    print('The name = ',end='')
    print(func.__name__)
    print('The class = ',end='')
    print(func.__class__)
    print('now =')
    func()
    
another_func(my_func)
another_func(second_func)
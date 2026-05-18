# -*- coding: utf-8 -*-
"""
Created on Mon May 31 08:29:47 2021

@author: Alvin
"""

class ComplexNumber:

    def __init__(self, r = 0, i = 0):
        """"初始化方法"""
        self.real = r 
        self.imag = i 

    def getData(self):
        print("{0}+{1}j".format(self.real, self.imag))

if __name__ == '__main__':
    c = ComplexNumber(5, 6)
    c.getData()

    c2 = ComplexNumber(50, 60)
    c2.getData()
    print(c2.real)
    print(c2.imag)
    c2.value2=100
    print(c2.value2)
    print(c2.real)
    print(c2.imag)
    
    print(c.value2)
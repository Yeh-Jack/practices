# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


class Parent:  # define parent class
    def myMethod(self):
        print("Calling parent method")


class Child(Parent):  # define child class
    def myMethod(self):
        print("Calling child method")

    def call_father_myMethod(self):
        Parent.myMethod(self)


class Child2(Parent):  # define child class
    pass


# def myMethod(self):
#    print ('Calling child method')

c = Child()  # instance of child
c.myMethod()  # child calls overridden method

c2 = Child2()
c2.myMethod()  # child calls overridden method

print("i want to call father method")
# c._Parent.myMethod()
c.call_father_myMethod()

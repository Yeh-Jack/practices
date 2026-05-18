# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


class Parent:  # define parent class  # Base class
    parentAttr = 100

    def __init__(self):
        print("Calling parent constructor")

    def parentMethod(self):
        print("Calling parent method")

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("Parent attribute :", Parent.parentAttr)


class Child(Parent):  # define child class  #衍生類別 (Derived)

    def __init__(self):
        print("Calling child constructor")

    def childMethod(self):
        print("Calling child method")


c = Child()  # instance of child
c.childMethod()  # child calls its method
c.parentMethod()  # calls parent's method
c.setAttr(200)  # again call parent's method
c.getAttr()  # again call parent's method

print("*****************")

p1 = Parent()
# p1.childMethod()      # child calls its method
p1.parentMethod()  # calls parent's method
p1.setAttr(500)  # again call parent's method
p1.getAttr()  # again call parent's method

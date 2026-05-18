# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 19:08:29 2023

@author: USER
"""

alist = [2, 3, 4, 5, 6]  # 0-4

print(alist[5])


# %%


alist = [2, 3, 4, 5, 6]  # 0-4

try:
    print(alist[5])

except IndexError:
    print("超出list的範圍")

print("gogogo")


# %%

try:
    x = int(input("Please enter age : "))
    if x < 18:
        raise NameError("年紀太小")

except ValueError:
    print("Oops!  That was no valid number.  Try again...")

except NameError:
    print("年紀太小~~~~!!!!!")

print("apple")

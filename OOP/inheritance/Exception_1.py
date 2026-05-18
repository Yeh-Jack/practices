# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 18:52:04 2023

@author: USER
"""

x = 10
y = "2"
print(x + y)  # TypeError

print("lccnet is good")

# %%

x = eval(input("請輸入x的值"))  # NameError
y = input("請輸入y的值")


print(x + y)  # TypeError:

print("lccnet is good")


# %%

x = int(input("Please enter a number: "))

# ValueError:

# %%
while True:
    try:
        # print(10 * (1/0))
        "2" + 2
        # x = int(input("Please enter a number: "))
        break

    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

    except ZeroDivisionError:
        print("分母為零")
        break

    except TypeError:
        print("type error")
        break


print("apple")

# %%
while True:
    x = int(input("Please enter a number: "))
    break

print("apple")

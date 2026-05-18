# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 19:26:57 2023

@author: USER
"""


def bool_return():
    try:
        # return True
        print(5 / 0)

    except:
        print("except occur")

    finally:  # 不管有或沒有發生例外，都會去執行的程式
        # return False
        print("finally")


bool_return()

# %%


def divide(x, y):
    try:
        result = x / y

    except (
        ZeroDivisionError
    ):  # 當執行try裡面的程式碼是，「有」發生ZeroDivisionError例外時，會去處理程式區段
        print("division by zero!")

    except (
        TypeError
    ):  # 當執行try裡面的程式碼是，「有」發生TypeError例外時，會去處理程式區段
        print("type ERROR!")

    else:  # 當執行try裡面的程式碼是，「沒有」發生任何例外時，會去處理程式區段
        print("result is", result)

    finally:  # 不管「有」或「沒有」發生例外，都會去執行的程式
        print("executing finally clause")


# divide(2, 1)

# divide(2, 0)

divide("2", "1")

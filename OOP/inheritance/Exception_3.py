# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 19:16:04 2023

@author: USER
"""

open("database.sqlite")

# %%

try:
    open("database.sqlite")


except FileNotFoundError:
    try:
        raise RuntimeError("unable to handle error")

    except RuntimeError:
        print("RuntimeError occur")

    except:
        print("except occur")

print("louis")


# %%


def func():
    raise ConnectionError


try:
    func()


except ConnectionError as exc:
    raise RuntimeError("RuntimeError") from exc

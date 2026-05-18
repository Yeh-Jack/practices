# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 20:03:11 2023

@author: USER
"""


class B(Exception):
    pass


class C(B):
    pass


class D(C):
    pass


for a in [B, C, D]:
    try:
        raise a()
    except B:
        print("B")
    except D:
        print("D")
    except C:
        print("C")
    # except B:
    #     print("B")

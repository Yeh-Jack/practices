# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 19:36:28 2023

@author: USER
"""

try:
    raise TypeError("bad type")


except Exception as e:
    # e.add_note('Add some information')
    e.add_note("Add some more information")
    raise


# %%
def f():
    raise OSError("operation failed")


excs = []


for i in range(3):  # 0 1 2
    try:
        f()
    except Exception as e:
        e.add_note(f"Happened in Iteration {i+1}")
        excs.append(e)

print(excs)

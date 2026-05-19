# -*- coding: utf-8 -*-
"""
Created on Mon May  2 13:25:14 2022

@author: cadtc
"""

import sqlite3
conn = sqlite3.connect('student.db')
print("Opened database successfully")

conn.execute('CREATE TABLE students (name TEXT,addr TEXT,city TEXT,pin TEXT)')
print("Table created successfully")
conn.close()

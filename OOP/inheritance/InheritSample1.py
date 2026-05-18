# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


class Date(object):
    def get_date(self):
        return "2025-12-12"

    def get_age(self):
        return "28"

    def get_hei(self):
        return "170"


class Time(Date):
    def get_time(self):
        return "20:30:30"


dt = Date()
print("Get date from Date class: ", dt.get_date())

tm = Time()
print("Get time from Time class: ", tm.get_time())
print("Get date from class by inheriting or calling Date class method: ", tm.get_date())
print("Get date from class by inheriting or calling Date class method: ", tm.get_age())

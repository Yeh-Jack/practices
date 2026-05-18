# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class JustCounter:
   __secretCount = 0
   abc=10

   def count(self):
      self.__secretCount += 1
      print(self.__secretCount)
         
counter = JustCounter()
counter.count()
counter.count()

print(counter.abc)

# print(counter.__secretCount)
#%%

counter2 = JustCounter()
print(counter.abc)  # 物件counter存取類別JustCounter的abc屬性(變數)
print(counter2.abc) # 物件counter2存取類別JustCounter的abc屬性(變數)
print(JustCounter.abc) # 類別JustCounter存取類別JustCounter的abc屬性(變數)

counter.abc=100    #物件counter設定自已物件內的abc屬性(變數)為100
print(counter.abc)  # 物件counter存取自已物件內的abc屬性(變數)
print(JustCounter.abc)  #類別JustCounter存取類別JustCounter的abc屬性(變數)
print(counter2.abc)   # 物件counter2存取類別JustCounter的abc屬性(變數)

counter2.abc=200    #物件counter2設定自已物件內的abc屬性(變數)為200
print(counter2.abc)  # 物件counter2存取自已物件內的abc屬性(變數)
print(JustCounter.abc)   #類別JustCounter存取類別JustCounter的abc屬性(變數)

counter2.abc=100
print(counter2.abc)

print(counter2.abc is counter.abc )


counter.abc=200 

print(counter2.abc is counter.abc )

#%%

#__secretCount

# print(counter.__secretCount)
print(counter._JustCounter__secretCount)

counter._JustCounter__secretCount=50

print(counter._JustCounter__secretCount)

counter.count()

#%%

print(counter2._JustCounter__secretCount)

counter2.count()

print(counter2._JustCounter__secretCount)

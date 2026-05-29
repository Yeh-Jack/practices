import pandas as pd

score = {"姓名":["皮卡丘", "寶石海星", "噴火龍", "鯉魚王"],
         "屬性":["電","水","火", "水"]}

data = pd.DataFrame(score)
#      姓名 屬性
# 0   皮卡丘  電
# 1  寶石海星  水
# 2   噴火龍  火
# 3   鯉魚王  水


# to_dict的預設為dict，轉換後的樣式為：{column(列名) : {index(行名) : value(值) )}}
print(data.to_dict("dict"))
# {'姓名': {0: '皮卡丘', 1: '寶石海星', 2: '噴火龍', 3: '鯉魚王'}, 
#  '屬性': {0: '電', 1: '水', 2: '火', 3: '水'}}


# 轉換後的樣式為：{column(列名) : Series (values) (值)}
print(data.to_dict("series"))
# {'姓名': 0     皮卡丘
# 1    寶石海星
# 2     噴火龍
# 3     鯉魚王
# Name: 姓名, dtype: object, '屬性': 0    電
# 1    水
# 2    火
# 3    水
# Name: 屬性, dtype: object}


# 轉換後的樣式為：{'index' : [index]，'columns' :[columns]，'data' : [values]}
print(data.to_dict("split"))
# {'index': [0, 1, 2, 3], 
#  'columns': ['姓名', '屬性'], 
#  'data': [['皮卡丘', '電'], ['寶石海星', '水'], ['噴火龍', '火'], ['鯉魚王', '水']]}


# 轉換後的樣式為：[{column(列名) : value(值)}…{column:value}]
print(data.to_dict("records"))
# [{'姓名': '皮卡丘', '屬性': '電'}, 
# {'姓名': '寶石海星', '屬性': '水'}, 
# {'姓名': '噴火龍', '屬性': '火'}, 
# {'姓名': '鯉魚王', '屬性': '水'}]


# 轉換後的樣式為：{index(值) : {column(列名) : value(值)}}
print(data.to_dict("index"))
# {0: {'姓名': '皮卡丘', '屬性': '電'}, 
#  1: {'姓名': '寶石海星', '屬性': '水'}, 
#  2: {'姓名': '噴火龍', '屬性': '火'}, 
#  3: {'姓名': '鯉魚王', '屬性': '水'}}

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_dict.html
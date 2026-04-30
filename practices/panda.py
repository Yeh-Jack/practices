import numpy as np
import pandas as pd
import json
import os

SKIP_ONE_LINE = "\n\n"
# cwd = os.getcwd()
cwd = os.getcwd() + "/.."
csvPath = cwd + "/data/csv/"
jsonPath = cwd + "/data/json/"
xmlPath = cwd + "/data/xml/"

data = {
    "Name": ["Adele", "BiBi", "Carol", "David", "Elon", "Frank"],
    "Country": ["China", "India", "Japan", "Korea", "ROC", "Vienum"],
    "Score": np.random.randint(60, 100, 6),
}
data = pd.DataFrame(data)
print(f"Source data\n{data}", end=SKIP_ONE_LINE)

# # --- Series
# data = pd.Series({"a": "Adele", "b": "BiBi", "c": "Carol"})
# print(data.index)
# print("-----" * 6)
# print(data.values, end=SKIP_ONE_LINE)

# # --- DataFrame
# scores = np.random.randint(1, 101, size=9).reshape(3, 3)
# df = pd.DataFrame(
#     scores, index=["Adele", "BiBi", "Carol"], columns=["Chinese", "English", "Math"]
# )
# print(df, end=SKIP_ONE_LINE)

# # --- Read CSV and JSON into DataFrame
# csv = pd.read_csv(
#     csvPath + "台灣電力公司113年度鄉鎮市別用電統計資料.csv", encoding="utf-8-sig"
# )
# print(csv)

# with open(jsonPath + "全台景點資料.json", encoding="utf-8-sig") as file:
#     jsn = json.load(file)["XML_Head"]["Infos"]["Info"]  # The jsn is a list.
# jsn = pd.DataFrame(jsn)  # Convert the list to a DataFrame.
# print(jsn.info())

# # --- Extract by .loc[] and .iloc[]
# data = np.arange(1, 13).reshape(3, 4)
# print(f"Source data:\n{data}", end=SKIP_ONE_LINE)
# data = pd.DataFrame(data)
# print(f"Extract 3rd column by data[2]:\n{data[2]}", end=SKIP_ONE_LINE)
# print(
#     f"Extract data by .loc[0:1, 2:3] (by column name) [inclusive:inclusive] :\n{data.loc[0:1, 2:3]}",
#     end=SKIP_ONE_LINE,
# )
# print(
#     f"Extract data by .iloc[:2, 2:4] (by column index) [inclusive:exclusive]:\n{data.iloc[:2, 2:4]}",
#     end=SKIP_ONE_LINE,
# )

# # --- Insert and replace
# data = pd.DataFrame(data)
# data.insert(4, 4, np.random.randint(60, 100, 3))  # Append a column
# data.insert(4, 5, np.random.randint(0, 60, 3))  # Insert a column
# data.loc[3] = np.random.randint(60, 100, 6)  # Append a row
# print(
#     f"Inserted data:\n{data}",
#     end=SKIP_ONE_LINE,
# )
# data.loc[3] = np.random.randint(0, 60, 6)  # Replace a row
# print(
#     f"Replace the last row:\n{data}",
#     end=SKIP_ONE_LINE,
# )

# # --- Concatenate
# df1 = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
# df2 = pd.DataFrame({"C": [5, 6], "D": [7, 8]})
# print(f"df1 :\n{df1}\ndf2 :\n{df2}", end=SKIP_ONE_LINE)
# result = pd.concat([df1, df2], axis=0)
# print(f"axis = 0: \n{result}", end=SKIP_ONE_LINE)
# result = pd.concat([df1, df2], axis=1)
# print(f"axis = 1: \n{result}", end=SKIP_ONE_LINE)

# df1 = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
# df2 = pd.DataFrame({"A": [5, 6], "B": [7, 8]})
# print(f"df1 :\n{df1}\ndf2 :\n{df2}", end=SKIP_ONE_LINE)
# result = pd.concat([df1, df2], axis=0)
# print(f"axis = 0: \n{result}", end=SKIP_ONE_LINE)
# result = pd.concat([df1, df2], axis=1)
# print(f"axis = 1: \n{result}", end=SKIP_ONE_LINE)

# # --- Filter data
# pickLoc = data.loc[data["Country"] == "ROC"]
# pickQuery = data.query("Country == 'ROC'")
# print(f"pickLoc\n{pickLoc}{SKIP_ONE_LINE}pickQuery\n{pickQuery}", end=SKIP_ONE_LINE)

# filter = 75
# pickLoc = data.loc[data["Score"] >= filter]
# pickQuery = data.query("Score >= @filter")
# print(f"pickLoc\n{pickLoc}{SKIP_ONE_LINE}pickQuery\n{pickQuery}", end=SKIP_ONE_LINE)

# # --- Sort data
# sort = data.sort_values("Score", ascending=False)
# print(f"Sorted:\n{sort}", end=SKIP_ONE_LINE)
# print(f"Top 3:\n{sort.head(3)}", end=SKIP_ONE_LINE)

# --- Grouping data
titanic = pd.read_csv(csvPath + "Titanic.csv")
grouped = titanic.groupby(["Pclass", "Sex", "Embarked"])
groupAge = grouped["Age"].mean()
pivot = groupAge.unstack(level="Sex")  # Pick a group as level
print(pivot, end=SKIP_ONE_LINE)
pivot = groupAge.unstack()  # Level is default to the last group.
print(pivot, end=SKIP_ONE_LINE)

pivot["Average"] = pivot.mean(axis=1)
pivot = pivot.reset_index()
print(pivot, end=SKIP_ONE_LINE)

SKIP_ONE_LINE = "\n\n"

# --- Basic mathmatical calculation.
# PI = 3.14159
# r = 5
# area = PI * r * r
# print(
#     "r = %d\tarea of the circle = %f\ndimension = %d\tlength = %f"
#     % (r, area, 2 * r, 2 * PI * r)
# )
# print("PI = %s\tr = %s\tarea = %s" % (type(PI), type(r), type(area)), end=SKIP_ONE_LINE)

# --- Input and output.
# inp = input("Input a value : ")
# inpVal = eval(inp)
# print(
#     "Your input is %s, and type of your input is %s.\nDigit : %f"
#     % (inp, type(inpVal), inpVal)
# )

# --- Reverse a string.
# string = "Hello world!"
# print(string[::-1], end=SKIP_ONE_LINE)

# --- String mainuplation.
# parts = string.split()
# print(f"type of parts = {type(parts)}, parts = {parts}")
# join = "_".join(parts)
# print(f"Joined string = {join}", end=SKIP_ONE_LINE)
# org = "Hello"
# to = "Hi,"
# print(f"Replace '{org}' by '{to}' -> {string.replace(org, to)}", end=SKIP_ONE_LINE)

# --- String encoding and decoding.
# string = "一二三四五 on the original Unicode."
# utf8 = string.encode()
# big5 = string.encode(encoding="big5")
# print(f"Original string = [{string}]")
# print(f"Encode it to UTF-8 = {utf8}")
# print(f"Encode it to BIG-5 = {big5}")
# print(f"Decode UTF-8 to UTF-8 = {utf8.decode(encoding="utf8")}")
# # UnicodeDecodeError: codec can't decode
# # print(f"Decode UTF-8 to BIG-5 = {utf8.decode(encoding="big5")}")
# # print(f"Decode BIG-5 to UTF-8 = {big5.decode(encoding="utf8")}")
# print(f"Decode BIG-5 to BIG-5 = {big5.decode(encoding="big5")}", end=SKIP_ONE_LINE)

# --- Numeric testing.
# nums = ["77", " 77", "７７", "七七", "77.77", "+77.77", "-77"]
# for num in nums:
#     print(
#         f"Testing .. [{num}] ->\tisDigital = {num.isdigit()}\tisDecimal = {num.isdecimal()}\tisNumeric = {num.isnumeric()}"
#     )
# print()

# --- Control flow.
# score = eval(input("Please input a score : "))
# if score < 0 or score > 100:
#     print(f"Invalid score number [{score}].")
# elif score >= 90:
#     print(f"[{score}] is excellent.")
# elif score >= 80:
#     print(f"[{score}] is great.")
# elif score >= 70:
#     print(f"[{score}] is good.")
# elif score >= 60:
#     print(f"[{score}] is fine.")
# else:
#     print(f"[{score}] is unsatisfied.")
# print()

# --- DivMod
# i, j = divmod(12, 7)
# print(f"12 / 7 = {i}, modular = {j}", end=SKIP_ONE_LINE)

# --- Enumerate
# cartoons = ["Dora", "Mulan", "Pica"]
# for idx, name in enumerate(cartoons, start=1):
#     string = "Player #{:0>3} is <{}>".format(idx, name)
#     print(f"{string}, hash = {hash(string)}")
# print()


# --- Map with custom function
# def translate(numStr: str, isCapital: bool) -> str:
#     base = ord("0")
#     numChars = ["零", "一", "二", "三", "四", "五", "六", "七", "八", "九"]
#     if isCapital == True:
#         numChars = ["零", "壹", "貳", "參", "肆", "伍", "陸", "柒", "捌", "玖"]
#     result = list()
#     for num in iter(numStr):
#         idx = ord(num) - base
#         result.append(numChars[idx])
#     return "".join(result)


# isCapital = input("是否轉為大寫中文(y/n)：").lower()
# if isCapital == "n":
#     isCapital = False
# else:
#     isCapital = bool(isCapital)

# nums = input("請輸入以 ',' 隔開的數字清單：").split(",")
# nums = list(map(str.strip, nums))

# string = list(map(lambda x: translate(x, isCapital), nums))
# print()
# for idx, trans in enumerate(string):
#     print(f"Translate #{idx:0>2} - [{nums[idx]}] = [{trans}].")
# print()

# --- Initiate a list(array)
# lst1 = [(100 + pow(i, 2)) for i in range(20) if (i % 2) == 0]
# lst2 = [(123 + pow(i, 2)) for i in range(0, 20, 4)]
# print("Original lists :")
# print(f"list1 = {lst1}")
# print(f"list2 = {lst2}", end=SKIP_ONE_LINE)

# print("Extend list1 from list2 :")
# lst1.extend(lst2)
# print(f"list1 = {lst1}", end=SKIP_ONE_LINE)

# print("Clone list2 to list4 :")
# lst4 = []
# lst4.extend(lst2)
# print(f"list4 = {lst4}", end=SKIP_ONE_LINE)

# --- List element removal.
# lst5 = [(100 + pow(i, 2)) for i in range(20) if (i % 2) == 0]
# print(f"list5 = {lst5}")
# del lst5[0]
# lst5.remove(200)
# print(f"Remove the first element and 200 = {lst5}", end=SKIP_ONE_LINE)

# firstOne = lst5.pop(0)
# lastOne = lst5.pop()
# print(f"First = {firstOne}, last = {lastOne}, remaind = {lst5}", end=SKIP_ONE_LINE)

# --- List (array) and tuple
# import copy

# lst1 = [[1, 2, 3], True, 3.14, "Good"]
# lst2 = lst1.copy()
# print(f"Original lists with shallow copy :\nlst1 = {lst1}\nlst2 = {lst2}")
# lst2[0][1] = 3
# lst2[0][2] = 5
# print(f"Modify on lst2 :\nlst1 = {lst1}\nlst2 = {lst2}", end=SKIP_ONE_LINE)

# lst1 = [[1, 2, 3], True, 3.14, "Good"]
# lst2 = copy.deepcopy(lst1)
# print(f"Original lists with deep copy :\nlst1 = {lst1}\nlst2 = {lst2}")
# lst2[0][1] = 3
# lst2[0][2] = 5
# print(f"Modify on lst2 :\nlst1 = {lst1}\nlst2 = {lst2}", end=SKIP_ONE_LINE)

# --- Random number
# import random

# random.seed("test")
# print(random.random())
# random.seed("test")
# print(random.random())

# if __name__ == "__main__":
#     print("This is the main entrance.")
# else:
#     print("This is NOT the main entrance.")

# --- Open file
# # Write mode : 'w' for replace mode, 'a' for append mode.
# file = open("./data/out.txt", "a")
# file.write("Hello!!\n")
# # Declare 'r' before Windows file name for 'raw string' mode.
# # print("Hello!!", file=open(r"C:\Python\out.txt", "w"))
# file.close()

# # Open file by 'with' : the file automatically closed in the end of the block.
# with open("./data/out.txt", "a") as file:
#     file.write("Hello!!\n")

# --- Exception handling
# a = input("Number A: ")
# b = input("Number B: ")

# try:
#     print(int(a) / int(b))
# except ValueError:
#     print("It's not integer number.")
# except ZeroDivisionError:
#     print("Divided by 0")
# except BaseException as e:
#     print(f"Unable to calculate. {e.__class__.__name__}: {e}")

# print("Finish.")

# --- Read CSV file
# import csv

# path = "./data/csv/"
# maleRows = []

# def extract(row, extCol):
#     data = []
#     for i in extCol:
#         data.append(row[i])
#     return data

# try:
#     with open(path + "Titanic.csv", encoding="UTF-8") as file:
#         all = list(csv.reader(file))
#         extCol = [2, 4, 7, 9]

#         row = all[0]
#         maleRows.append(extract(row, extCol))

#         for row in all:
#             if row[3] == "male" and row[10] == "Q":
#                 maleRows.append(extract(row, extCol))

#     print(
#         f"There was {len(maleRows)} male on boarded from 'QueensTown', all passengers = {len(all)-1}.",
#         end=SKIP_ONE_LINE,
#     )

#     extractFile = path + "maleQ.csv"
#     with open(extractFile, "w", encoding="UTF-8") as file:
#         fw = csv.writer(file)
#         # fw.writerow(all[0])
#         fw.writerows(maleRows)

#     print(f"Data extracted and saved to {extractFile}.", end=SKIP_ONE_LINE)

# except BaseException as e:
#     print(f"Failed on file operation: {e}", end=SKIP_ONE_LINE)


# --- Read XML file.
# import os
# import xml.etree.ElementTree as ET

# cwd = os.getcwd()
# print(f"Current working directory: {cwd}")

# path = "./data/xml/"
# root = ET.parse(path + "宜蘭縣停車場.xml").getroot()

# for row in root.findall("row_item"):
#     data = []
#     for col in ["名稱", "編號", "小車位總數", "小車位剩餘數"]:
#         data.append(row.find(col).text)
#     print(f"{data[0]}({data[1]})\t小車位數 = {data[3]} / {data[2]}")

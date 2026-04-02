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

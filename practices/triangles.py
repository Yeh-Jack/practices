# 直角三角形(由少變多)
for i in range(1, 6):
    print(i * "*")

# *
# **
# ***
# ****
# *****


# 直角三角形(由多變少)
for i in range(5):
    print((5 - i) * "*")

# *****
# ****
# ***
# **
# *


# 直角三角形(由少變多)
for i in range(1, 6):
    print(" " * (5 - i) + "*" * i)

#     *
#    **
#   ***
#  ****
# *****


# 直角三角形(由多變少)
for i in range(5, 0, -1):
    print(" " * (5 - i) + "*" * i)

# *****
#  ****
#   ***
#    **
#     *


# 等腰三角形(由少變多)
rows = 5  # 設定行數
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

#     *
#    ***
#   *****
#  *******
# *********


# 等腰三角形(由多變少)
rows = 5  # 設定行數
for i in range(rows, 0, -1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

# *********
#  *******
#   *****
#    ***
#     *


# 菱形(分成上下兩半輸出)
rows = 5  # 設定半菱形的高度(即菱形的一半）
# 上半部分(包含中間行)
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

# 下半部分(不包含中間行）
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "*" * (2 * i - 1))


# 菱形(分成上下兩半輸出，另一種寫法)
rows = 5  # 設定半菱形的高度即菱形的一半）
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "* " * i)


# 菱形(一次輸出)
rows = 5  # 設定行數
for i in range(-(rows - 1), rows):
    # 控制空白
    for j in range(1, abs(i) + 1):
        print(" ", end="")
    # 控制星星
    for z in range(1, (rows + 1) - abs(i)):
        print("* ", end="")
    print()

#     *         ,,,,*
#    * *        ,,,* *
#   * * *       ,,* * *
#  * * * *      ,* * * *
# * * * * *     * * * * *
#  * * * *      ,* * * *
#   * * *       ,,* * *
#    * *        ,,,* *
#     *         ,,,,*

import math


def baseCalculate(a, b, c):
    return pow(b, 2) - (4 * a * c)


a = int(input("請輸入 a："))
b = int(input("請輸入 b："))
c = int(input("請輸入 c："))
base = baseCalculate(a, b, c)
print(f"\nBase calculation = {base} -> ", end="")

if base < 0:
    print("無解！")
elif base == 0:
    result = -b / (2 * a)
    print(f"只有一個答案：{result}")
else:
    result = math.sqrt(base)
    print(f"有兩個答案：{(-b+result)/(2*a)}, {(-b-result)/(2*a)}")
print()

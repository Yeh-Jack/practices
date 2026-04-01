amount = int(input("請輸入購買金額："))

if amount >= 100000:
    amount *= 0.69
elif amount >= 55000:
    amount *= 0.78
elif amount >= 25000:
    amount *= 0.88
elif amount >= 10000:
    amount *= 0.95

print(f"則扣後價格為：{amount}")

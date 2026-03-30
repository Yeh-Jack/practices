height = eval(input("請輸入身高 (cm)："))
weight = eval(input("請輸入體重 (kg)："))
heightM = height / 100
bmi = weight / (heightM * heightM)
print(f"\n身高{height:>5.2f}cm, 體重{weight:>5.2f}kg, BMI = {bmi:>5.2f}.", end="\n\n")

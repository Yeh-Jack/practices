height=eval(input("請輸入身高 (m)："))
weight=eval(input("請輸入體重 (kg)："))
bmi=weight/(height*height)
print(f"\n身高{height:>5.2f}m, 體重{weight:>5.2f}kg, BMI = {bmi:>5.2f}.", end="\n\n")

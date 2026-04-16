import random

cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
cardIdx = random.randint(0, 12)

counter = 0
upper = 12
lower = 0
pick = ""
while True:
    if pick == "":
        print("請輸入紙牌數字：", end="")
    pick = input().upper()

    try:
        pickIdx = cards.index(pick)
        counter = counter + 1
        if pickIdx == cardIdx:
            print(f"猜對了，紙牌數字是：{cards[cardIdx]}，您總共猜了 {counter} 次。")
            break
        elif cardIdx < pickIdx:
            if upper >= pickIdx:
                upper = pickIdx - 1
        else:
            if lower <= pickIdx:
                lower = pickIdx + 1
        print(
            f"猜錯了，紙牌數字介於 {cards[lower]} ~ {cards[upper]}，請重新輸入：",
            end="",
        )
    except Exception as err:
        print(
            f"您輸入了錯誤的紙牌數字：{pick}，或者發生錯誤：{err}，請重新輸入：",
            end="",
        )
        pick = "X"  # In case user inputs "".

print()

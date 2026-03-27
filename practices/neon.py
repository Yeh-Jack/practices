import time

# 初始狀態為最右邊的燈亮著
INITIAL_STATE = 0b00000001
TURNOVER_STATE = 0b10000000
lights = INITIAL_STATE  # 這確實是二進制，但直接輸出時會顯示1(十進制)

print("按下 Ctrl+C 可以停止程式\n")

try:
    while True:
        # ①將數字轉為8位二進制字串
        # bin(lights) 強制python用二進制方式呈現，會得到0b1
        # 只取1出來，然後再使用zfill()會檢查字串長度，若不足8位會補0
        binary_str = bin(lights)[2:].zfill(8)

        # ②美化顯示結果，將1變成紅圈、0變成白圈
        visual = binary_str.replace("1", "🔴").replace("0", "⚫")

        # ③輸出結果
        print(f"\r目前燈光狀態：[{visual}]  位元值: {binary_str}", end="")

        # ④位元左移：讓燈往左跑
        lights = lights << 1

        # ⑤循環邏輯：如果燈跑出了8位元範圍，就重設回1
        if lights > TURNOVER_STATE:
            lights = INITIAL_STATE

        time.sleep(0.25)

except KeyboardInterrupt:
    print("\n\n霓虹燈已關閉！")

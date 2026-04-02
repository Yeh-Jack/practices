# 將num的字串編譯成程式碼後，再用eval()或exec()函數執行
num = "2*8+1"


# 由於num只有單一表達示，所以mode用eval
result = compile(num, "string", "eval")
print(eval(result))         # 17
print(exec(result))         # None
# compile()會將字串2*8+1編譯成python可執行的數學運算式
# eval會有回傳值，因此執行後會得到17這個值
# exec回傳值永遠為None，故執行後會得到None

import time
# 方式 1：compile() + eval()
# num = "print(f\"2*8+1={2*8+1}\")"
compiled_code = compile(num, "PrintCalculation", "eval")
start_time = time.time()
for _ in range(100000):
    eval(compiled_code)
print("使用 compile() 的時間:", time.time() - start_time)
        # 使用 compile() 的時間: 0.019000530242919922

# 方式 2：直接 eval()
start_time = time.time()
for _ in range(100000):
    eval(num)
print("直接 eval() 的時間:", time.time() - start_time)
        # 直接 eval() 的時間: 0.5680234432220459

# compile() + eval()只需要編譯1次，後續需要使用時可以直接使用
# 因此執行效率較高，適用在需要大量重複計算時
# 直接 eval()時每次都要重新解析字串
# 因此執行效率低，建議用在單次或少量計算時


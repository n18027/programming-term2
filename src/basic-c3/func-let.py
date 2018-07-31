# 関数を定義
def mul_func(a, b):    # a + b を掛け算する関数
    return a * b

def div_func(a, b):    # aをbで割る関数
    return a / b
# mul_func関数に変数をだいにゅう
func = mul_func
# 代入した変数で関数を使う
result = func(2, 3)
print(result)

# div_func関数を変数を代入する場合
func2 = div_func
result = func2(10, 5)
print(result) # 表示結果

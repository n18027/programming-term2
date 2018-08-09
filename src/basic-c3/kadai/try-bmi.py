# BMI 判定（例外処理あり版）
# ユーザーから正しい値w得てBMIを計算
while True:
    try:    # breakするまで繰り返す
        #入力
        weight = float(input("体重(kg)は？"))
        height = float(input("身長(cm)は？"))
        # BMI の計算
        height = height / 100 # m に直す
        bmi = weight / (height * height)
        break;
    except:
        print("入力ミスがあります。再度入力してください")

result = ""
if bmi < 18.5: result = "痩せ型"
elif bmi < 25: result = "標準体重"
elif bmi < 30: result = "肥満(軽)"
else: result = "肥満(重)"

print("BMI :", bmi)
print("判定:", result)

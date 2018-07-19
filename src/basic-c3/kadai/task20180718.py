menu = {
    "DripCoffee": 280,
    "ColdBrewCoffee": 320,
    "CafeLatte": 330,
    "SoyLatte": 380,
    "Cappuccino": 330,
    "CaramelFrappuccino": 470,
    "MacchaCreamFrappuccino": 470}

option = {
    "LowFatMilk": 0,
    "NonFatMilk": 0,
    "SoyMilk": 50,
    "DeepCoffee": 60,
    "WhipCream": 70,
    "CaramelShrup": 60,
    "ChocoSource": 0,
    "DeCafe": 50}
tyumon = []
summing = []
staba = True
while staba:
    print("メインメニューを選んでください")
    your_manu = input(">>")
    if your_manu == "" or your_manu == "q":
        print("キャンセルされました。")
        staba = False
    else:
        if your_manu in your_manu.keys():
            print("メインメニューを承りました。")
            tyumon.append(your_manu)
            summing.append(manu[your_manu])
            staba = False
staba2 = True
            while staba2:
                print("オプションをつけてください")
                your_option = input()
                if your_option == "" or your_option == "q":
                    print("オプションはつけません。")
                    print("ご注文は", tyumon, "です。")
                    print("合計金額は", manu[your_manu], "円です")
                    staba2 = False
                else:
                    print("選択されたオプションはありません")
        else:
            print("選択されたオプションはありません")

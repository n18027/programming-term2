import random

shake_dice = int(input("サイコロを振ってくだちい"))
go_forword = 0

while True:
    if sum(go_forword) < 10:
        shake_dice = random.randint(1, 6)
        print("playerは現在" + str(shake_dice)+"マス進んでいます")
        go_forword.append(shake_dice)
        masu = sum(go_forword)
        print("playerは現在" + str(masu)+"マス進んでいます")
        if masu == go_forword:
            print("player goal")
            break
    elif sum(go_forword) > 10:
        sai = random.randint(1, 6)
        print("playerは現在" + str(shake_dice)+"マス進んでいます")
        go_forword.append(shake_dice)
        masu = sum(go_forword)
        print("playerは現在" + str(masu)+"マス進んでいます")
        if masu == go_forword:
            print("player goal")
            break

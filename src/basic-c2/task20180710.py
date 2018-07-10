print("何を出しますか？1:グー、2:チョキ、3:パー")

your_ken = input(">> ")

if your_ken == "1":
    print("CPUはパーを出しました。当然のようにあなたは負けます")
elif your_ken == "2":
    print("CPUはグーを出しました。まぁ負けますよねそりゃー。")
elif your_ken == "3":
    print("CPUはチョキをだしました。あなたは負けです。")
else:
    print("入力が不正です。終了します。")

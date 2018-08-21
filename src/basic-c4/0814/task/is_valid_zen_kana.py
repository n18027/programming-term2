import re

print("全角カナの文字を入力してください")
kana = input(">>")
pattern = u"[ァ-ン]"

if re.search(pattern, kana):
    print("{}は全角カナのみの文字列です".format(kana))
else:
    print("{}に全角カナ以外が含まれています".format(kana))

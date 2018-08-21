import re

print("メールアドレスを入力してください")
mail = input(">>")
pattern = r"[a-zA-Z0-9]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9]+$"

if re.match(pattern, mail):
    print("{}はメールアドレスの形式です".format(mail))
else:
    print("{}はメールアドレスの形式ではありません".format(mail))

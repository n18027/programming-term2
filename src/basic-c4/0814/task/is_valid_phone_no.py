import re

print("電話番号を入力してください")
phone = input(">>")
pattern = r"^\d{2,4,3}-\d{2, 4}-\d{3, 4}"

if re.search(phone, pattern):
    print("{}は電話番号の形式です".format(phone))
else:
    print("{}は電話番号の形式ではありません".format(phone))

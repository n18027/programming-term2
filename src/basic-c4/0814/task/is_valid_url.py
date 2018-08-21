import re

print("URLを入力してください")
URL = input(">>")
pattern = r"https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"

if re.match(pattern, URL):
    print("{}はURLの形式です".format(URL))
else:
    print("{}はURLの形式ではありません".format(URL))

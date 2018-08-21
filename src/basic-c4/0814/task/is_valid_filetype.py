import re

print("ファイル名を入力してくだいさい")
filename = input(">>")
txt = r"\w.txt$"

if re.search(txt, filename):
    print("{}は拡張子が.txtのテキストファイルです".format(filename))
else:
    print("{}は拡張子が.txtのテキストファイルではありません".format(filename))

# 正規表現パターンをコンパイル
zipre = re.compile(r"^[0-9]{3}\-[0-9]{4}$")
# 正しい正規表現
zipre.search("440-0012")
# 不正な正規表現
print(ziper.search("111:1-2222"))

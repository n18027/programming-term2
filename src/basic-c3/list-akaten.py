points = [88, 76, 23, 14, 29, 80, 91]
# 30点未満のデータだけ選んで赤点リストに追加
akaten = []
for p in points:
    if p < 30:
        akaten.append(p)

# 選んだデータを表示
print(akaten)

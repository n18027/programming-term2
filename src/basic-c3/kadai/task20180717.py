import random

seiza = [
    "牡羊座",
    "牡牛座",
    "双子座",
    "蟹座",
    'しし座',
    '乙女座',
    "てんびん座",
    "蠍座",
    "射手座",
    '山羊座',
    "水瓶座",
    "魚座"]
unsei = ["最高", "今日死にます", "いつもと変わらない日常"]
color = ["赤", "とっても赤", "赤以外はだめ", "赤を赤で染めた赤"]
ad = ["何もかもが最悪うまく行かない",
      "何もかもがうまく行くワンちゃん宝くじ当たります",
      "借金取りに目をつけられて最悪な一日に友達との縁をすべて切りましょう"]
i = random.randint(0, len(seiza)-1)
u = random.randint(0, len(unsei)-1)
c = random.randint(0, len(color)-1)
a = random.randint(0, len(ad)-1)
print("占い: 今日の{0}座の運勢は{1}。{3}。ラッキーカラーは{2}です！".format(seiza[i], unsei[u], color[c], ad[a]))

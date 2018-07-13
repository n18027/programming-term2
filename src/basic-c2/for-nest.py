# 今年の年月と曜日を組み合わせて表示するプログラム

# 曜日を判定するためのカウンタ
counter_for_dow = 0
# 曜日を表すカウンタ(1月1日は月曜日)
dow_idx = 0
# 日〜土の名称を持つ文字列
dow_str = ""
# 曜日と月の組み合わせが正しいか
is_valid_date = True

# 1月から12月まで繰り返し
for month in range(1, 13):
    # 1日から31日まで繰り返し
    for day in range(1, 32):
        # 日付の妥当性チェックの結果を一旦Trueで初期化
        is_valid_date = True

        if (month == 2) and (day > 28):
            # 2月は28日まで
            is_valid_date = False
        elif (month == 4) or (month == 6) or (month == 9) or (month == 11):
            if day > 30:
                # 4,6,9,11月は30日まで
                is_valid_date = False

        # 不正な日付は出力しない
        if not is_valid_date:
            continue

        # 日付が正しいので、曜日を判断する
        counter_for_dow += 1
        # カウンタを7で割って曜日を求める
        dow_idx = counter_for_dow % 7
        # 曜日のインデックス(0:日〜6:土)が出たので表示用に変換
        if dow_idx == 0:
            dow_str = "日"
        elif dow_idx == 1:
            dow_str = "月"
        elif dow_idx == 2:
            dow_str = "火"
        elif dow_idx == 3:
            dow_str = "水"
        elif dow_idx == 4:
            dow_str = "木"
        elif dow_idx == 5:
            dow_str = "金"
        elif dow_idx == 6:
            dow_str = "土"

        # 日付と曜日を表示
        print("{0}月{1}日({2})".format(month, day, dow_str))

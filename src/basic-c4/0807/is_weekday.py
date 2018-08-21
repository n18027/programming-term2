from datetime import datetime, timedelta

def process(target_date):
    """
    メインロジックを実行する
    Parameters
    ----------
    target_date : datetime
        処理対象の日付
    Returns
    -------
    list
        表示されるメッセージを要素に含むリスト
    """

    res_list = []   # 結果として返すリスト

    return res_list

def display(msgs):
    """
    結果を表示する
    Parameters
    ----------
    msgs: list
        表示するメッセージが格納されたリスト
    Returns
    -------
    なし
    """
    print(*msgs, sep="\n")

# メイン処理
if __name__ == '__main__':
    while True:
        try:
            input_date = input('日付を入力してください。')
            target_date = datetime.strptime(input_date, '%Y/%m/%d')

            display(process(target_date))
            break
        except:
            print('入力された日付が不正です。再入力してください。')

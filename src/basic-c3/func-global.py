# 関数の外側でvalueに100を代入
value = 100

def changeValue():
    """
    グローバル変数を変更する

    Paramenters
    -----------
    なし

    Returns
    -------
    なし
    """

    # ぐろーばる宣言
    global value
    # 関数の内側でvalueを変更
    value = 20

changeValue()
print("value=", value)

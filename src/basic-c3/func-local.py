#  関数の外側でvalueに100を代入
value = 100

def changevalue():
    """
    値を変更する

    Paramentrs
    ----------
    なし

    Returns
    -------
    なし
    """
    #　関数の内側でvalueを変換
    value = 20

changevalue()
print("value=", value)

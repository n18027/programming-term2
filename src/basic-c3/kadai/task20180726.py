import random
goal_pos = 10
cur_x = 0
def shake_dice():
    shake_dice = random.randit(1, 6)
    return shake_dice
def go_forward():
    go_forward += shake_dice
    return go_forward
while go_forward < goal_pos:
    player = input("サイコロを振りなんし")
    if player != "":
        continue
    if go_forward < goal_pos:
        print("{}が出ました。現在地は{}です".format(shake_dice, go_forward))
        continue
    break
print("{}が出ました。クリアー".format(shake_dice))

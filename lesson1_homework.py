import random


# 定义猜拳函数。1 代表石头， 2 代表剪刀 3 代表布
def finger_guessing_game():
    # 电脑生成1-3的随机数字代表 石头剪刀布
    com_hand = random.randint(1, 3)
    # 获取玩家的输入
    human_hand = int(input('1石头, 2剪刀, 3布, come on: '))

    # 如果玩家没有获胜，就一直玩下去
    while human_hand - com_hand != -1 and human_hand - com_hand != 2:
        # 如果是平手， 提示平手
        if human_hand == com_hand:
            print("平手，再来")
        # 否则就是电脑赢了
        else:
            print('电脑赢了，再来')
        # 无论是平手还是电脑赢了，都重新获得双方的输入
        human_hand = int(input('1石头, 2剪刀, 3布, come on: '))
        com_hand = random.randint(1, 3)
    # 恭喜玩家，结束
    print('恭喜你')


finger_guessing_game()
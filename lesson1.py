# 求圆的面积
def get_around_area():
    # 定义PI 为3.14
    pi = 3.14

    # 用户输入圆的半径 r
    r = input("请输入圆的半径: ")
    r = int(r)

    # 用公式 area = pi 乘以 r 的平方
    area = pi * r ** 2

    # 输出面积到屏幕
    print(area)


# 判断奇偶数
def odd_or_even():
    # 获取用户输入的整数
    number = int(input("请输入一个整数: "))
    # 判断是不是奇偶数
    # 如果number对2取模 等于 0
    if number % 2 == 0:
        # 输出 even
        print("even")
    # 否则
    else:
        # 输出 odd
        print('odd')


# 随机在1-10中间，选择一个数字，作为答案。提示用户输入你猜的数字。
# 如果你没猜对，会告诉你是猜大了还是猜小了，并且要求你继续输入数字。
# 如果你猜对了。你在第几次猜对了。如果你第一次就猜对，会有一个特别的祝贺语。
def guess_number_game():
    # 获取一个 随机的答案，并且范围在1-10
    import random
    answer = random.randint(1, 10)
    # 获取用户的输入，一个整数（1-10）
    number = int(input("请输入一个1-10的整数: "))
    # 定义一个次数，用于后面输出提示语
    n = 1

    # 如果没有猜对，就一直执行下面的步骤
    while number != answer:
        # 如果猜大了
        if number > answer:
            # 提示你猜大了，并且重新输入
            number = int(input("猜大了，请重新输入: "))
        # 否则
        else:
            # 提示你猜小了，并且重新输入
            number = int(input("猜小了，请重新输入: "))
        n += 1

    # 如果不是第一次
    if n != 1:
        # 恭喜你，在第N次猜对了
        print("恭喜你，在第{}次猜对了".format(n))
    # 否则
    else:
        # 厉害，第一次就猜对了
        print("厉害，第一次就猜对了")


get_around_area()
odd_or_even()
guess_number_game()


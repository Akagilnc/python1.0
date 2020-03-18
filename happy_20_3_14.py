x, odd = 1, 3
n = 1
flag = False
times = int(input('please input times: '))
while n < times:
    if flag:
        x += 1 / odd
    else:
        x -= 1 / odd
    flag = not flag
    odd += 2
    n += 1
print(x * 4)

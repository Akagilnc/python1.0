# 变量，datatype, .func()
a_num = 2
a_float = 2.0

a_str = '1'
b_str = 'b'
c_str = 'list'
d_str = 'xyz'
e_str = 'c_str'
e_str_strip = 'temp with empty right    '.strip()

a_list = [1, 'dict', 2.0]

b_list_with_add = [1, 2, 3].append(4)

value = '1'
key = 'abc'
a_dict = {'key': 'value', 'key2': 'value'}
b_dict = {value: key}

c_dict_get_value = {'value': 'key'}.get('value')


# input, process, output
# step by step, flow control, when to stop
def add_1(x=1, y=1):
    print('add function')
    return x + y


result_1 = int(add_1('1', '1'))

add_1()

for x in [1, 2, 3]:
    print(x)

x = 1
while x == 1:
    print(x)
    x += 1


# : and indent （while judge,for in list and dict）
def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(n, m):
    return n * m


def div(x, y):
    return x / y


def calculate(x, y, operation):
    if operation == '+':
        return add(x, y)
    if operation == '-':
        return sub(x, y)
    if operation == '*':
        return mul(x, y)
    if operation == '/':
        return div(x, y)
    return 'wrong operation, operation should like + - * /'


result = calculate(2, 3, '*')
result3 = calculate(calculate(5, 5, '*'), 10, '*')  # 250

# 函数 IPO， params and return

# 函数套用，流程

# 字符串，format

# file, with open vs open close

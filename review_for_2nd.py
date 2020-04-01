# 变量，datatype, .func()
a_num = 2
a_float = 2.0
a_str = '1'
b_str = 'b'
c_str = 'list'
d_str = 'dict'
e_str_strip = 'temp with empty right    '.strip()
a_list = [1, 'dict', 2.0]
b_list_with_add = [1, 2, 3].append(4)
a_dict = {'key', 'value'}
b_dict = {'value', 'key'}
c_dict_get_value = {'value': 'key'}.get('value')


# : and indent （while judge,for in list and dict）
def add(x, y):
    pass


def sub(x, y):
    pass


def mul(x, y):
    pass


def div(x, y):
    pass


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


# 函数 IPO， params and return

# 函数套用，流程

# 字符串，format

# file, with open vs open close

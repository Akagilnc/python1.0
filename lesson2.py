# 创建文件+写入内容
def create_file():
    # 创建文件
    file = open('lesson2.txt', 'w', encoding='utf_8_ig')
    # 写入内容
    file.write('ak, 32, it, m\n')
    file.write('lily, 28, hr, f\n')
    file.write('tiger, 35, it, m\n')
    file.write('lisa, 22, hr, f\n')
    # 关闭文件
    file.close()


# 读取并做处理
def read_and_refactor():
    # 打开文件
    data = open('lesson2.txt')
    # 依次取出每一条记录,存储在变量中
    result = []
    for line in data:
        name, age, department, sex = line.split(', ')
        # 把记录写入一句话的模版里。 name 今年 age 岁，
        # 是一个XXXX的根据性别来称呼
        if sex.strip() == 'm':
            desc = '一个阳光男孩'
        else:
            desc = '一个美丽冻人的小姐姐'
        result.append('{name}今年{age}岁，{desc}\n'.format(name=name, age=age, desc=desc))
    data.close()
    return result


# 存储结果到一个新的文件
def write_result(input_data):
    # 打开文件
    file = open('lesson2_report.txt', 'w')
    # 写入内容
    file.writelines(input_data)
    # 关闭文件
    file.close()


# create_file()
contents = read_and_refactor()
write_result(contents)

# 建立文件，创建文件+填充内容
def create_file():
    # 打开文件，写的模式
    file = open('lesson2.txt', 'w')
    # 写入内容
    file.write('ak, 30, it, m\n')
    file.write('lily, 28, hr, f\n')
    file.write('tiger, 32, it, m\n')
    file.write('flower, 22, hr, f\n')
    # 关闭文件
    file.close()


# 读取文件，改变内容，形成一个结果
def read_file():
    # 读取内容
    # 打开文件，读的模式
    file = open('lesson2.txt', 'r')
    # 生成一个结果数据，写一段话来描述这个员工的情况
    # 一行一行的读取数据
    result_list = []
    for line in file:
        # 信息分别保存到name, age, depart, sex四个变量里面
        name, age, depart, sex = line.split(', ')
        # 根据每行信息，来生成最终的结果
        # 如果他是一个m，描述是 "阳光可爱的大男孩"
        if sex.rstrip() == 'm':
            desc = "阳光可爱的大男孩"
        # 如果她是一个f，描述是 "美丽冻人的小姐姐"
        else:
            desc = "美丽冻人的小姐姐"
        # 生成我们的结果，存储
        result = "这位是{name:<8}, 属于{depart}部门，今年{age}岁，是一个{desc}.\n".format(
            name=name, depart=depart, age=age, desc=desc
        )
        result_list.append(result)
    # 关闭文件
    file.close()
    return result_list


# 写入一个新的结果文件
def write_file(contents):
    # 打开文件，写的模式
    file = open('report.txt', 'w', encoding='utf_8_sig')
    # 写入数据
    file.writelines(contents)
    # 关闭文件
    file.close()


# 调用部分
create_file()
results = read_file()
write_file(contents=results)

# for loop 一件一件的取出已知集合里面的元素。然后一条一条来循环处理
# while loop 当满足条件，一直执行，直到条件不满足

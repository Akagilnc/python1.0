# 创建数据文件
def create_file():
    # 打开文件
    origin_file = open('l2_homework.txt', 'w')
    # 定义写入的数据list
    origin_data = ['name, size_s, size_m, size_l\n',
                   '小黄鸭, 2, 5, 12\n',
                   '鲸鱼玩偶, 2, 7, 4\n',
                   '奥特曼, 3, 1, 8\n',
                   '路飞手办, 6, 2, 3\n',
                   '高达模型, 9, 1, 2\n']
    # 写入文件
    origin_file.writelines(origin_data)
    # 关闭文件
    origin_file.close()


# 读取文件
def read_file():
    # 打开文件
    file = open('l2_homework.txt')
    # 去掉第一行标题
    file.readline()
    # 定义结果集list
    results = []
    # 依次读取数据
    for row in file:
        # 分解数据到变量 name, num_s, num_m, num_l
        name, num_s, num_m, num_l = row.split(', ')
        # 去掉末尾的回车
        num_l = num_l.rstrip()
        # 求汇总数量 count
        count = int(num_s) + int(num_m) + int(num_l)
        # 生成结果集所需格式的描述
        result = '商品名称：{name:^8}，有S号{}个，M号{}个，L号{}个，合计{}个.\n'.format(num_s, num_m, num_l, count, name=name)
        # 保存结果到结果集list
        results.append(result)
    # 关闭文件
    file.close()
    # 返回结果集
    return results


# 写入报告文件
def write_file(contents):
    # 打开文件
    # 写入结果集
    # 关闭文件
    with open('l2_homework_report.txt', 'w') as file:
        file.writelines(contents)


create_file()
result_list = read_file()
write_file(result_list)



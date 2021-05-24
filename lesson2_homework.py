def create_file(file_name):
    file = open(file_name, 'w', encoding='utf_8')
    file.write('代码 名称 最新价 涨跌幅 涨跌额 成交量(手) 成交额 振幅 最高 最低 今开 昨收 量比 换手率 市盈率(动态) 市净率\n')
    file.write(
        '688037 芯源微 131.85 12.00% 19.35 7.77万 9.74亿 24.81% 135.00 107.09 107.09 112.50 1.73 43.95% 9036.44 14.67\n')
    file.write(
        '688058 宝兰德 178.50 9.25% 16.60 1.66万 2.77亿 15.00% 179.50 155.21 156.00 161.90 1.64 18.25% 254.00 7.60\n')
    file.write('600555 海航创新 3.14 8.18% 0.29 102.80万 3.18亿 7.72% 3.14 2.92 2.95 2.85 2.43 10.56% -62.00 3.07\n')
    file.write('600683 京投发展 4.46 10.00% 0.41 13.67万 5871.48万 15.06% 4.46 3.85 3.85 4.05 2.83 1.85% -100.25 1.25\n')
    file.write('600869 智慧能源 3.90 -3.11% 0.45 148.12万 6.98亿 16.63% 4.90 4.16 4.32 4.45 1.20 6.67% 25.36 2.10\n')
    file.close()


def read_and_process(file_name):
    # 读取源文件
    data_file = open(file_name, encoding='utf_8')
    # 初始化一个结果集
    results = []
    # 依次读取每一条记录
    for line in data_file:
        # 去掉第一行的title
        if line.startswith('代码'):
            continue
        # 取出所有的数据，分割之后赋予不同的变量
        # code, name, price, change, change_range, volume, value, amplitude, \
        #     high, low, open_today, close_yesterday, qrr, turnover, pe, pb =
        infos = line.split(' ')
        code, name, open_today, price, change, pb = infos[0], infos[1], infos[10], infos[11], infos[3], infos[-1]
        # 把涨跌幅转化为float类型
        change = float(change.strip("%"))
        # 根据涨跌幅的具体范围，确定状态
        if 0 < change < 10:
            status = '上涨'
        elif -10 < change < 0:
            status = '下跌'
        elif change == 10:
            status = '涨停'
        elif change == -10:
            status = '跌停'
        elif change > 10:
            status = '新股'

        # 生成我们的单条报告描述
        result = '{} {}: 今日开盘价为{}, 收盘价为{}, {}, 市净率为{}'.format(code, name, open_today, price, status, pb)
        # 把单条报告保存到结果集
        results.append(result)

    # 关闭文件，返回结果集
    data_file.close()
    return results


# 保存到文件
def save_to_file(file_name, input_data_list):
    # 打开文件，写入模式
    file = open(file_name, 'w', encoding='utf_8')
    # 保存内容
    file.writelines(input_data_list)
    # 关闭文件
    file.close()


# create_file('origin.txt')
contents = read_and_process('origin.txt')
save_to_file('lesson2_homework_report.txt', contents)

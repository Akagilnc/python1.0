def create_file():
    file = open("l2_hw_origin.txt", "w", encoding='utf_8')
    file.write(
        "688037 芯源微 131.85 12.00 19.35 7.77万 9.74亿 24.81 135.00 107.09 107.09 112.50 1.73 43.95% 9036.44 14.67\n")
    file.write("688058 宝兰德 178.50 9.25 16.60 1.66万 2.77亿 15.00 179.50 155.21 156.00 161.90 1.64 18.25% 254.00 7.60\n")
    file.write("600555 海航创新 3.14 8.18 0.29 102.80万 3.18亿 7.72 3.14 2.92 2.95 2.85 2.43 10.56% -62.00 3.07\n")
    file.write("600683 京投发展 4.46 10.00 0.41 13.67万 5871.48万 15.06 4.46 3.85 3.85 4.05 2.83 1.85% -100.25 1.25\n")
    file.write("600869 智慧能源 3.90 -3.11 0.45 148.12万 6.98亿 16.63 4.90 4.16 4.32 4.45 1.20 6.67% 25.36 2.10\n")
    file.close()


def read_and_process_file():
    data = open("l2_hw_origin.txt", encoding='utf_8')
    result = []
    for line in data:
        # 代码code 名称name 最新价price 涨跌幅change 涨跌额change_range 成交量(手)volume 成交额turnover 振幅amplitude
        # 最高high 最低low 今开open_today 昨收close_yesterday 量比qrr 换手率turnover 市盈率(动态)pe 市净率pb
        # 与下一条2选一
        code, name, price, change, change_range, volume, turnover, amplitude, \
            high, low, open_today, close_yesterday, qrr, turnover, pe, pb = line.split(" ")

        # 与上一条二选一，利用list的元素选择也可以这样写
        infos = line.split(" ")
        code, name, open_today, price, change, pb = infos[0], infos[1], infos[10], infos[2], infos[3], infos[-1]

        # 去掉末尾的%，附加题答案
        change = float(change.strip('%'))

        # 根据涨跌幅设置描述语
        if 10 > change > 0:
            desc = "上涨"
        elif 0 > change > -10:
            desc = "下跌"
        elif change == 10:
            desc = "涨停"
        elif change == -10:
            desc = "跌停"
        elif change > 10:
            desc = "新股"
        result.append("{} {}：今日开盘价为{}，收盘价为{}，{}，市净率为{}".format(
            code, name, open_today, price, desc, pb))

    data.close()
    return result


# 保存结果到新文件
def save_result_to_file(input_data):
    report = open("l2_hw_report_daily.txt", "w", encoding='utf_8')
    report.writelines(input_data)
    report.close()


create_file()
contents = read_and_process_file()
save_result_to_file(contents)

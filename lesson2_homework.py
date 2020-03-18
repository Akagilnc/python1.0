# def create_file():
#     file = open("origin.txt","w")
#     file.write("688037 芯源微 131.85 12.00 19.35 7.77万 9.74亿 24.81 135.00 107.09 107.09 112.50 1.73 43.95% 9036.44 14.67\n")
#     file.write("688058 宝兰德 178.50 9.25 16.60 1.66万 2.77亿 15.00 179.50 155.21 156.00 161.90 1.64 18.25% 254.00 7.60\n")
#     file.write("600555 海航创新 3.14 8.18 0.29 102.80万 3.18亿 7.72 3.14 2.92 2.95 2.85 2.43 10.56% -62.00 3.07\n")
#     file.write("600683 京投发展 4.46 10.00 0.41 13.67万 5871.48万 15.06 4.46 3.85 3.85 4.05 2.83 1.85% -100.25 1.25\n")
#     file.write("600869 智慧能源 3.90 -3.11 0.45 148.12万 6.98亿 16.63 4.90 4.16 4.32 4.45 1.20 6.67% 25.36 2.10\n")
#     file.close()
#
# create_file()

def read_and_process_file():
    data = open("origin.txt")
    result = []
    for line in data:
# 代码code 名称name 最新价currentp 涨跌幅fluc 涨跌额range 成交量(手)volume 成交额turnover 振幅amplitude
# 最高high 最低low 今开open 昨收close 量比qrr 换手率turnover 市盈率(动态)pe 市净率pb
        code, name, currentp, fluc, range, volume, turnover, amplitude, high, low, open, close, qrr, turnover, pe, pb = line.split(" ")
        fluc = fluc.strip()
        if 10 > fluc > 0:
            desc = "上涨"
        elif 0 > fluc > -10:
            desc = "下跌"
        elif fluc == 10:
            desc = "涨停"
        elif fluc == -10:
            desc = "跌停"
        elif fluc > 10:
            desc = "新股"
        result.append("{} {}：今日开盘价为{}，收盘价为{}，{}，市净率为{}\n".format(code,name,open,close,fluc,pe))
    data.close()
    return result


def save_result_to_file(input_data):
    report = open("report_daily.txt","w")
    report.write(input_data)
    report.close()


contents=read_and_process_file()
save_result_to_file(input_data=contents)
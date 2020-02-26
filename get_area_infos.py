import pandas as pd
from datetime import datetime
import json


# 读取历史数据内容
def read_file():
    with open('conv.json', encoding='utf_8') as file:
        return json.load(file)['results']


# 写入汇总数据
def write_infos_to_excel(input_data, writer):
    df = pd.DataFrame(input_data,
                      index=[datetime.fromtimestamp(info.get('updateTime') / 1000).strftime('%Y-%m-%d %H:%M:%S')
                             for info in input_data],
                      columns=['provinceName', 'confirmedCount', 'curedCount', 'deadCount'])
    df.to_excel(writer, sheet_name='上海市')
    writer.save()


# 获得区域信息
def get_area_info(input_data):
    # 初始化保存区域信息的字典。每个区域都为一个key, value里面存入这个区域的所有信息的list。
    area_info_dict = {}
    # 依次读取每一条信息
    for infos in input_data:
        # 获取地区信息
        area_info = infos.get('cities')
        # 获取这条数据的更新时间，并转化为YYYY-MM-DD HH:MM:SS的格式
        update_time = datetime.fromtimestamp(infos.get('updateTime') / 1000).strftime('%Y-%m-%d %H:%M:%S')
        # 检查是否找到了地区信息，针对某些前期数据没有地区信息的情况
        if area_info:
            # 遍历所有的地区信息
            for info in area_info:
                # 获取地区名称，并且因为区域名称有差异，去掉末尾的新和区字
                area_name = info['cityName'] = info['cityName'].strip('新区')
                # 给本条区域信息附加上更新时间
                info['updateTime'] = update_time

                # 如果地区名已存在，直接把当前信息添加进列表
                if area_info_dict.get(area_name):
                    area_info_dict[area_name].append(info)
                # 如果不存在且把当前信息作为一个列表的第一条元素传入
                else:
                    area_info_dict[area_name] = [info]

    # 返回构建好的区域信息字典
    return area_info_dict


# 将区域信息写入到各自的sheet里
def write_area_infos_to_excel(input_area_infos, writer):
    # 从区域信息字典内取出 key和value，并且用pandas生成每一个区域的DataFrame,
    # 然后再写入到一个excel文件的不同sheet里
    for city_name, infos in input_area_infos.items():
        df = pd.DataFrame(infos,
                          # 指定更新时间为index，简写 for 循环
                          index=[info['updateTime'] for info in infos],
                          # columns的参数表示，只获取这些列，别的不要
                          columns=['cityName', 'confirmedCount', 'curedCount', 'deadCount'])

        # 实际写入操作。再writer.save()的时候完成
        df.to_excel(writer, sheet_name=city_name)
        writer.save()


data = read_file()
data = list(reversed(data))
# 创建最终汇总的excel文件
writer = pd.ExcelWriter('area_infos.xlsx')
write_infos_to_excel(data, writer)
area_infos = get_area_info(data)
write_area_infos_to_excel(area_infos, writer)
writer.close()

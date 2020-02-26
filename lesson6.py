import pandas as pd
import os
from datetime import datetime


# 读取一个excel文件
def get_infos_from_one_file(filename):
    return pd.read_excel('./files/{}'.format(filename),
                         engine='openpyxl',
                         usecols=['provinceName', 'confirmedCount', 'curedCount',
                                  'deadCount', 'country', 'updateTime'])


# 获取所有最新数据
def get_all_latest_infos():
    # 获得该目录下所有的文件名
    filenames = os.listdir('./files')
    # 初始化一个总的信息变量，DataFrame
    all_infos = pd.DataFrame()
    # 一个一个的取出文件名
    for filename in filenames:
        # 根据文件名获取信息
        data = get_infos_from_one_file(filename)
        # 找到最新的信息
        info = data.iloc[data['updateTime'].idxmax()]
        # 重命名当条信息，然后把它插入的DataFrame
        info = info.rename(datetime.fromtimestamp(info['updateTime'] / 1000).strftime('%Y-%m-%d %H:%M:%S'))
        info = info.drop('updateTime')
        all_infos = all_infos.append(info)
    return all_infos


# 求一个df汇总信息
def get_sum_info(input_df, sum_drop_name, df_drop_name):
    sum_info = input_df.sum()
    sum_info = sum_info.rename('汇总')
    sum_info[sum_drop_name] = ""
    input_df = input_df.append(sum_info)
    input_df = input_df.drop(columns=[df_drop_name])

    return input_df


# 存入一个文件的不同sheet 用pandas
def write_to_single_file(input_chn_df, input_oversea_df, filename):
    with pd.ExcelWriter('{}.xlsx'.format(filename)) as file:
        input_chn_df.to_excel(file, sheet_name='China')
        input_oversea_df.to_excel(file, sheet_name='Oversea')
        file.save()


infos = get_all_latest_infos()

df_china = infos[infos.country == '中国']
df_oversea = infos[infos.country != '中国']
df_china_with_sum = get_sum_info(df_china, 'provinceName', 'country')
df_oversea_with_sum = get_sum_info(df_oversea, 'country', 'provinceName')

write_to_single_file(df_china_with_sum, df_oversea_with_sum, 'conv_latest')

# df_china_with_sum.to_excel('conv_china_latest.xlsx')
# df_oversea_with_sum.to_excel('conv_oversea_latest.xlsx')

import json


# 将本课API端口采集到的中国的全国最新疫情数据汇总写入txt文件
def get_china_latest_and_save():
    file = open('lesson3.json', encoding='utf_8')
    data = json.load(file).get('data')
    file.close()

    result = '{}, 中国 累计确诊{}, 死亡{}, 治愈{}, 现存确诊{}, 现存重症{} \n'.format(
        data.get('times'), data.get('gntotal'), data.get('deathtotal'),
        data.get('curetotal'), data.get('econNum'), data.get('heconNum')
    )

    save_to_file(result, 'l3_hw_china_latest.txt')


# 拿到最新的中国分省市的数据，写入txt文件
def get_china_area_and_save():
    file = open('lesson3.json', encoding='utf_8')
    data = json.load(file).get('data')
    file.close()

    china_area_infos = data.get('list')
    time = data.get('times')
    result = []
    for info in china_area_infos:
        result.append('{}, {}, 累计确诊{} 现存确诊{} 较昨日{} 死亡{} 治愈{} \n'.format(
            time, info.get('name'), info.get('value'), info.get('econNum'),
            info.get('conadd'), info.get('deathNum'), info.get('cureNum')
        ))

    save_to_file(result, 'l3_hw_china_area_latest.txt')


# 拿到最新的海外分国家的数据并写入txt文件
def get_oversea_area_and_save():
    file = open('lesson3.json', encoding='utf_8')
    data = json.load(file).get('data')
    file.close()

    oversea_area_infos = data.get('otherlist')
    time = data.get('times')
    result = []
    for info in oversea_area_infos:
        result.append('{}, {}, 累计确诊{} 死亡{} 治愈{} \n'.format(
            time, info.get('name'), info.get('conNum'),
            info.get('deathNum'), info.get('cureNum')
        ))

    save_to_file(result, 'l3_hw_oversea_area_latest.txt')


# 保存指定data到指定文件
def save_to_file(input_data_list, file_name):
    file = open(file_name, 'w', encoding='utf_8')
    file.writelines(input_data_list)
    file.close()


get_china_latest_and_save()
get_china_area_and_save()
get_oversea_area_and_save()


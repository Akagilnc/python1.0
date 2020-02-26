import requests
import json
from datetime import datetime


# 调用远程API来获取数据
def call_api():
    # 定义地址
    address = 'https://lab.isaaclin.cn/nCoV/api/area?latest=0&province=上海市'
    # 调用，并获取信息
    data = requests.get(address)
    # 保存到一个json文件
    with open('2019_conv_shanghai_history.json', 'w') as file:
        json.dump(data.json(), file, ensure_ascii=False, indent=4)


# call_api()

def get_infos():
    # 获得字典格式的数据
    with open('2019_conv_shanghai_history.json') as file:
        data = json.load(file)

    # 获得所有的历史数据
    infos = data['results']

    # 打开需要写入的文件
    with open('l4_hw_history.txt', 'w') as file:
        # 依次取出历史数据
        for info in infos:
            # 获得更新时间的时间戳，并转换为datetime时间格式
            update_time = datetime.fromtimestamp(info.get('updateTime') / 1000)

            # 写入文件
            file.write('截止{}，{}，确诊人数为{}，治愈人数为{}，死亡人数为{}\n'.format(
                # 把时间格式化成中文友好的格式
                update_time.strftime('%Y年%m月%d日 %H:%M:%S'),
                info.get('provinceName'),
                info.get('confirmedCount'),
                info.get('curedCount'),
                info.get('deadCount')
            ))


get_infos()

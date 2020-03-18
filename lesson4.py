import requests
import json


# 调用远程API来获取数据
def call_api():
    # 定义地址
    address = 'https://lab.isaaclin.cn/nCoV/api/area?latest=0&province=上海市'
    # 调用，并获取信息
    data = requests.get(address)
    # 保存到一个json文件
    with open('2019_conv_shanghai_history.json', 'w', encoding='utf_8') as file:
        json.dump(data.json(), file, ensure_ascii=False, indent=4)


call_api()


# 处理信息
def get_info():
    # 打开文件
    with open('2019_conv.json') as file:
        data = json.load(file)
    # 获取我们results信息
    infos = data['results'][0]
    # 打印汇总信息
    with open('l4_hw.txt', 'w') as file:

        file.write('最新消息，{}，确诊人数为{}，治愈人数为{}，死亡人数为{}'.format(
            infos.get('provinceName'),
            infos.get('confirmedCount'),
            infos.get('curedCount'),
            infos.get('deadCount')
        ))

    # 分区信息
    # 获取分区信息
    details = infos['cities']
    # 取出里面的所有节点，并打印详细信息
    with open('l4_hw_details.txt', 'w') as file:
        for city in details:
            file.write('{}，确诊人数为{}，治愈人数为{}，死亡人数为{}\n'.format(
                city['cityName'],
                city['confirmedCount'],
                city['curedCount'],
                city['deadCount']
            ))


# get_info()

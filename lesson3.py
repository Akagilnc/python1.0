import __hello__
import requests
import json


__hello__

# 调用API获得最新的疫情数据，并保存到一个json文件
def call_api_and_save_to_file():
    # 调用API
    data = requests.get('https://interface.sina.cn/news/wap/fymap2020_data.d.json')
    # 打开文件
    file = open('lesson3.json', 'w', encoding='utf_8')
    # 保存文件
    json.dump(data.json(), file, ensure_ascii=False, indent=4)
    # 关闭文件
    file.close()


# 读取文件，并且获得海外疫情汇总数据，并打印到屏幕
def read_and_process():
    # 读取json文件
    file = open('lesson3.json', encoding='utf_8')
    contents = json.load(file)

    # 找到我们的海外疫情数据
    infos = contents.get('data').get('othertotal')

    # 打印数据 模板“截止今日，海外疫情 确诊 较昨日， 死亡 较昨日， 治愈 较昨日”
    template = '截止今日，海外疫情 确诊{} 较昨日{}， 死亡{} 较昨日{}， 治愈{} 较昨日{}'
    print(template.format(
        infos.get('certain'), infos.get('certain_inc'),
        infos.get('die'), infos.get('die_inc'),
        infos.get('recure'), infos.get('recure_inc')
    ))


# call_api_and_save_to_file()
read_and_process()

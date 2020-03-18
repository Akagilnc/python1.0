import requests
import json


# 调用api,获得返回的结果，并保存到文件
def call_api_and_save_results_to_json_file():
    # 定义我们的调用地址
    address = 'https://interface.sina.cn/news/wap/fymap2020_data.d.json'
    # 调用这个地址，得到返回结果
    response = requests.get(address)
    # 返回结果保存到json文件
    with open('lesson3.json', 'w', encoding='utf_8') as file:
        json.dump(response.json(), file, ensure_ascii=False, indent=2)


# 读取json文件，并且做处理，拿到最新的海外疫情数据
def read_file_and_process():
    # 读取一个json文件
    with open('lesson3.json', encoding='utf_8') as data_file:
        data = json.load(data_file).get('data')

    # 拿到海外数据
    oversea_data = data.get('othertotal')

    # 模板“截止今日，海外数据为 xxxxxxx ”
    print('截止今日，海外疫情最新数据， 确诊： {} 较昨日 {}， 死亡： {} 较昨日 {}， 治愈： {} 较昨日 {}'.format(
        oversea_data.get('certain'), oversea_data.get('certain_inc'),
        oversea_data.get('die'), oversea_data.get('die_inc'),
        oversea_data.get('recure'), oversea_data.get('recure_inc')
    ))
# call_api_and_save_results_to_json_file()


read_file_and_process()

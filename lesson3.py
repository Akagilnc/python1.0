# 读取文件
def read_file():
    with open('lesson3.txt') as file:
        return file.read()


# 处理得到的信息，获得2句话，一句是前五位品牌名称的。一句是出货量
def get_info(input_contents):
    # 分割句子
    infos = input_contents.split('，')
    # 初始化品牌句子，和出货量句子
    brand_info = sell_info = ""
    for temp in infos:
        # 获取品牌句子
        if '智能手机' in temp:
            brand_info = temp
        # 获取出货量句子
        if '出货量分别为' in temp:
            sell_info = temp

    # 返回两个句子
    return brand_info, sell_info


# 分解信息
def split_info(start_keyword, end_keyword, split_keyword, content):
    # 初始化开始的索引位置，结束的索引位置
    start_idx, end_idx = None, None

    # 获取开始和结束的位置
    if start_keyword is not None:
        start_idx = content.find(start_keyword)
    if end_keyword is not None:
        end_idx = content.find(end_keyword)
    # 截取 从开始到结束的 句子
    info = content[start_idx:end_idx]

    # 分割信息并返回
    return info.split(split_keyword)

contents = read_file()
content_list = contents.split('。')
brand, sell = get_info(content_list[0])
brand_info = split_info(start_keyword='三星', end_keyword='智能', split_keyword='、', content=brand)
sell_info = split_info('2', None, '、', sell)

print(brand_info)
print(sell_info)
for i in range(5):
    print("2019年，智能手机市场排名第{}的品牌是{}，全年手机出货量是{}".format(
        i + 1, brand_info[i], sell_info[i]
    ))

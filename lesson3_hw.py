# 读取文件
def read_file(file_name):
    with open(file_name, encoding='utf_8_sig') as file:
        return file.read()


# 处理得到的信息，截取所需内容语句
def get_info(input_contents, keywords):
    # 初始化返回变量
    info = ""
    # 如果文件内容不包含输入关键词
    if keywords not in input_contents:
        print("没有找到相关内容")
    else:
        # 用句号分割成句子
        sentences = input_contents.split('。')
        # 找到包含关键词的语句并返回
        for sentence in sentences:
            # 用逗号分割成语句
            phrases = sentence.split('，')
            # 找寻含有关键词的语句
            for phrase in phrases:
                if keywords in phrase:
                    info = phrase
    return info


# 分解语句中的信息，整理成列表
def split_info(start_keyword, end_keyword, split_keyword, content):
    # 初始化开始的索引位置、结束的索引位置
    start_idx, end_idx = None, None
    # 获取开始和结束的位置
    if start_keyword is not None:
        start_idx = content.find(start_keyword)
    if end_keyword is not None:
        end_idx = content.find(end_keyword)
    # 截取 从开始到结束的 语句
    info = content[start_idx + len(start_keyword):end_idx]
    # 分割信息并返回
    return info.split(split_keyword)


# 将列表内容写入文件
def write_file(inputs, file_name):
    import csv
    with open(file_name, 'w', encoding='utf_8_sig') as file:
        writer = csv.writer(file)
        writer.writerow()




# 生成报告
def get_reports(brands_infos, ext_infos, report_template, n):
    reports = []
    for i in range(n):
        line = (report_template.format(
            i + 1, brands_infos[i], ext_infos[i]
        ))
        reports.append(line)
    return reports


# 调取函数
contents = read_file('lesson3.txt')
# 分割成包含关键词的语句，注意指定关键词不可在其他语句中出现
brand_sentence = get_info(contents, '智能手机')
shipment_sentence = get_info(contents, '出货量分别为')
share_sentence = get_info(contents, '市场份额')
# 摘取所需信息并存为列表
brands = split_info('全年、', '智能手机', '、', brand_sentence)
shipments = split_info('分别为', None, '、', shipment_sentence)
shares = split_info('分别为', None, '、', share_sentence)
# 获取报告
reports1 = get_reports(brands, shipments, "2019年全年智能手机出货量第{}的品牌为{}，出货量为{}。\n", 5)
reports2 = get_reports(brands, shares, "2019年全年智能手机出货量第{}的品牌为{}，份额为{}。\n", 3)
# 写入品牌、市场份额报告
write_file(reports1, 'lesson3_class.txt')
write_file(reports2, 'lesson3_hw.txt')

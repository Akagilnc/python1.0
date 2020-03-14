from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome import options
import time
import random
import pandas as pd


def get_links(page):
    chrome_options = options.Options()
    chrome_options.headless = True
    with webdriver.Chrome(chrome_options=chrome_options) as driver:
        driver.get('http://www.ciaps.org.cn/quote/list-htm-catid-596.html')
        link_list = []
        for i in range(1, page+1):
            if i != 1:
                driver.find_element_by_css_selector('body > div:nth-child(9) > div.m_l.f_l > div > div.catlist > div > a:nth-child(5)').click()
                time.sleep(random.randrange(2, 6))
            links = driver.find_elements_by_css_selector('body > div:nth-child(9) > div.m_l.f_l > div > div.catlist > ul > li')
            for link in links:
                if link.get_attribute('class') == 'catlist_sp':
                    continue
                a_tag = link.find_element_by_tag_name('a')
                link_list.append(a_tag.get_attribute('href'))
        return link_list


def get_daily_data(input_link):
    chrome_options = options.Options()
    chrome_options.headless = True
    with webdriver.Chrome(chrome_options=chrome_options) as driver:
        driver.get(input_link)
        try:
            date = driver.find_element_by_css_selector('body > div:nth-child(11) > div.m_l.f_l > div > div.info').text
            date = date[8:]
            table_content = driver.find_element_by_css_selector('#content > table', ).text
        except NoSuchElementException:
            date = table_content = ""
        return date, table_content


def get_daily_price_data(input_date, input_info):
    data = []
    if input_info != " ":
        rows = input_info.split('\n')
        titles = rows[0].split(' ')

        for i in range(1, len(rows)):
            row = rows[i].split(' ')
            data_dict = dict(zip(titles, row))
            data_dict.update(日期=input_date)
            data.append(data_dict)
    else:
        pass
    return data


df = pd.DataFrame()
links = get_links(2)
for link in links:
    date, content = get_daily_data(link)
    prices = get_daily_price_data(date, content)
    df1 = pd.DataFrame(prices)
    df = df.append(df1)

df.to_excel('battery_price_20200313.xlsx')

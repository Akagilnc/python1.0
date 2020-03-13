from selenium import webdriver
from selenium.webdriver.chrome import options
import time
import random

chrome_options = options.Options()
chrome_options.headless = True
with webdriver.Chrome(chrome_options=chrome_options) as driver:
    driver.get('http://www.ciaps.org.cn/quote/list-htm-catid-596.html')
    for i in range(1, 3):
        if i != 1:
            driver.find_element_by_css_selector('body > div:nth-child(9) > div.m_l.f_l > div > div.catlist > div > a:nth-child(5)').click()
            time.sleep(random.randrange(2, 6))
        links = driver.find_elements_by_css_selector('body > div:nth-child(9) > div.m_l.f_l > div > div.catlist > ul > li.catlist_li')
        for link in links:
            a_tag = link.find_element_by_tag_name('a')
            print(a_tag.get_attribute('href'))





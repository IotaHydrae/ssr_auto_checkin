import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
chrom_driver = 'E:/driver/chromedriver.exe'
browser = webdriver.Chrome(executable_path=chrom_driver)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--start-maximized')  # 最大化运行（全屏窗口）,不设置，取元素会报错
chrome_options.add_argument('--disable-infobars')  # 禁用浏览器正在被自动化程序控制的提示
chrome_options.add_argument('--incognito')  # 隐身模式（无痕模式）
chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面
print('运行中。。。')
# browser.get('http://www.baidu.com/')
# input = browser.find_element_by_id('kw')
# input.send_keys('test')
# submit = browser.find_element_by_id('su')
# submit.click()
browser.get('http://kexue.ga/')
login = browser.find_element_by_tag_name('nav')
login.find_element_by_tag_name('a')
login.click()
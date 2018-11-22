#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/21 19:52
# @Author  : Ryu
# @Site    : 
# @File    : myselenium.py
# @Software: PyCharm

from selenium import webdriver
chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument('--headless')       #不显示浏览器弹窗
driver=webdriver.Chrome('F:\chromedriver.exe',options=chrome_options)
driver.get('https://music.163.com/#/song?id=483671599')
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
driver.switch_to_frame('g_iframe')
driver.find_element_by_xpath('//a[contains(@class,"znxt"]')[0].text

tests=driver.find_element_by_xpath('//')

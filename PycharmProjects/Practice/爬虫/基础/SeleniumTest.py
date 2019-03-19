#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/3/19 14:47
# software: PyCharm
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome(executable_path = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
browser.get("http://www.baidu.com")
# assert "Python" in browser.title
elem = browser.find_element_by_name("wd") # name
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
print(browser.page_source)

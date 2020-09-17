#!/usr/bin/env python3

# python3 -m pip install selenium

# download gecko webdriver

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Firefox()
driver.get("https://dominos.com/en/")

time.sleep(4)
click_sign_in = driver.find_element_by_xpath("/html/body/header/nav[1]/div[1]/div[3]/span/a")
click_sign_in.send_keys(Keys.RETURN)

time.sleep(3)
driver.find_element_by_xpath('//*[@id="Email"]').send_keys("sams.test.dev@gmail.com")
time.sleep(2)

time.sleep(1)
driver.find_element_by_xpath('//*[@id="Password"]').click()
driver.find_element_by_xpath('//*[@id="Password"]').send_keys("yumyumyumyumyumyum" + Keys.RETURN)
time.sleep(3)

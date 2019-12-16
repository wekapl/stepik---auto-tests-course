import os
from cmath import sin

from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)

    alert = browser.switch_to.alert
    alert.accept()

    x_element1 = browser.find_element_by_xpath(".//span[@id='input_value']")
    x1 = x_element1.text
    y = str(math.log(abs(12 * math.sin(int(x1)))))

    input1 = browser.find_element_by_css_selector("input.form-control")
    input1.send_keys(y)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()

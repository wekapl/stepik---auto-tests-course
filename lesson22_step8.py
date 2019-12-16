import os
from cmath import sin

from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_xpath("//input[@name='firstname']")
    input1.send_keys('firstname')
    input1 = browser.find_element_by_xpath("//input[@name='lastname']")
    input1.send_keys('lastname')
    input1 = browser.find_element_by_xpath("//input[@name='email']")
    input1.send_keys('email')

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'text.txt')  # добавляем к этому пути имя файла
    element = browser.find_element_by_xpath("//input[@name='file']")
    element.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)


finally:
    time.sleep(10)
    browser.quit()

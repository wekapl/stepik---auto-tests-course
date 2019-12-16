from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element1 = browser.find_element_by_xpath(".//span[@id='num1']")
    x1 = x_element1.text
    x_element2 = browser.find_element_by_xpath(".//span[@id='num2']")
    x2 = x_element2.text
    y = str(int(x1) + int(x2))

    from selenium.webdriver.support.ui import Select

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(y)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)


finally:
    time.sleep(10)
    browser.quit()

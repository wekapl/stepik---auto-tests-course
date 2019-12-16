from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_xpath(".//img")
    y = calc(x_element.get_attribute("valuex"))

    input1 = browser.find_element_by_xpath("//div/input[@id='answer']")
    input1.send_keys(y)
    option1 = browser.find_element_by_css_selector("[value='robots']")
    option1.click()
    option2 = browser.find_element_by_css_selector("[id='robotCheckbox']")
    option2.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)


finally:
    time.sleep(10)
    browser.quit()

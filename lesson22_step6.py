from cmath import sin

from selenium import webdriver
import time
import math

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element1 = browser.find_element_by_xpath(".//span[@id='input_value']")
    x1 = x_element1.text
    y = str(math.log(abs(12*math.sin(int(x1)))))

    input1 = browser.find_element_by_xpath("//input[@id='answer']")
    input1.send_keys(y)
    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option1)
    option1.click()
    option2 = browser.find_element_by_css_selector("[for='robotsRule']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()

    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    time.sleep(1)


finally:
    time.sleep(10)
    browser.quit()

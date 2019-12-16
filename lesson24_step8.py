import math
import time

from selenium import webdriver

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium import webdriver

    browser = webdriver.Chrome()
    # browser.implicitly_wait(5)
    browser.get(link)

    button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    button = browser.find_element_by_id("book")
    button.click()

    x_element1 = browser.find_element_by_xpath(".//span[@id='input_value']")
    x1 = x_element1.text
    y = str(math.log(abs(12 * math.sin(int(x1)))))

    input1 = browser.find_element_by_css_selector("input.form-control")
    input1.send_keys(y)

    button = browser.find_element_by_id("solve")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

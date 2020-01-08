from selenium import webdriver
import time
import unittest

# try:
from selenium.webdriver.chrome.webdriver import WebDriver


class TestAbs(unittest.TestCase):
    def test_1_welcome_text(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser: WebDriver = webdriver.Chrome()
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_xpath \
            (".//input[@placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_xpath \
            (".//input[@placeholder='Input your last name']")
        input2.send_keys("Broshka")
        input3 = browser.find_element_by_xpath \
            (".//input[@placeholder='Input your email']")
        input3.send_keys("ivan@test.io")
        input4 = browser.find_element_by_xpath \
            (".//input[@placeholder='Input your phone:']")
        input4.send_keys("11111111")
        input5 = browser.find_element_by_xpath \
            (".//input[@placeholder='Input your address:']")
        input5.send_keys("Swin street 9")
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text_el = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        # def test_welcome_text(self):
        self.assertEqual(
            "Congratulations! You have successfully registered!", welcome_text_el,
            "Congratulations! You have successfully registered!_1")
        # finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_2_welcome_text(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser: WebDriver = webdriver.Chrome()
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_xpath \
            (".//input[@placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_xpath \
            (".//input[@placeholder='Input your last name']")
        input2.send_keys("Broshka")
        input3 = browser.find_element_by_xpath \
            (".//input[@placeholder='Input your email']")
        input3.send_keys("ivan@test.io")
        input4 = browser.find_element_by_xpath \
            (".//input[@placeholder='Input your phone:']")
        input4.send_keys("11111111")
        input5 = browser.find_element_by_xpath \
            (".//input[@placeholder='Input your address:']")
        input5.send_keys("Swin street 9")
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text_el = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        # def test_welcome_text(self):
        self.assertEqual(
            "Congratulations! You have successfully registered!", welcome_text_el,
            "Congratulations! You have successfully registered!_2")
        # finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

    if __name__ == "__main__":
        unittest.main()

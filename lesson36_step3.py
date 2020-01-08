import pytest
import time
import math

from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link_tst',
                         ["236895/step/1", \
                          "236896/step/1", \
                          "236897/step/1", \
                          "236898/step/1", \
                          "236899/step/1", \
                          "236903/step/1", \
                          "236904/step/1", \
                          "236905/step/1"])
class TestSeeLink(object):
    def test_see_link(self, browser, link_tst):
        link = f"https://stepik.org/lesson/{link_tst}/"
        browser.get(link)

        input1 = browser.find_element_by_xpath \
            (".//textarea[@placeholder='Напишите ваш ответ здесь...']")
        answer = math.log(int(time.time()))
        input1.send_keys(str(answer))

        button = browser.find_element_by_xpath \
            (".//button[@class='submit-submission']")
        button.click()

        correct_text_elt = browser.find_element_by_xpath \
            (".//pre[@class='smart-hints__hint']")
        correct_text = correct_text_elt.text

        assert "Correct!" == correct_text

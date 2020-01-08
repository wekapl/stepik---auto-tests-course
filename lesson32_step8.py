import math
import time

from selenium import webdriver

try:
    def test_input_text(expected_result, actual_result):
        assert expected_result == actual_result, f"expected {expected_result}, got {actual_result}"


    test_input_text(81, 18)
finally:
    time.sleep(1)

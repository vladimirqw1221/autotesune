import time

from pages.buse_page import BasePage
from pages.element_page import TextBoxPage


def test_test_box(driver):
    test_test_box = TextBoxPage(driver, "https://demoqa.com/text-box")
    test_test_box.open()
    test_test_box.fill_all_filed()
    time.sleep(3)
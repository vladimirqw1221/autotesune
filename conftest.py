import time

import pytest as pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function')
def driver():
    driver  = webdriver.Chrome(executable_path='/Users/user/Desktop/resourse/chromedriver')
    driver.maximize_window()
    yield driver
    driver.quit()

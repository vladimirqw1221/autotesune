from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self ,driver ,url):
        self.driver = driver
        self.url = url




    def open(self):
        self.driver.get(self.url)


    def elemeny_is_clicable(self , locator , timeout=5):
        return wait(self.driver,timeout).until(EC.element_to_be_clickable(locator))

    def elemenys_are_visiber(self , locator , timeout=5):
        return wait(self.driver,timeout).until(EC.visibility_of_all_elements_located(locator))

    def elemenys_are_prisents(self , locator , timeout=5):
        return wait(self.driver,timeout).until(EC.presence_of_all_elements_located(locator))

    def elemeny_not_visiber(self , locator , timeout=5):
        return wait(self.driver,timeout).until(EC.invisibility_of_element_located(locator))

    def elemeny_is_visiber(self , locator , timeout=5):
        return wait(self.driver,timeout).until(EC.visibility_of_element_located(locator))


    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)










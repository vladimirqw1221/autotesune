import time

from locators.elements_page_locators import TextElementsLocators
from pages.buse_page import BasePage


class TextBoxPage(BasePage):
    locators = TextElementsLocators()


    def fill_all_filed(self):
        self.elemeny_is_visiber(self.locators.FULL_NAME).send_keys("scsc")
        self.elemeny_is_visiber(self.locators.EMAIL).send_keys("dkcs@scs.com")
        self.elemeny_is_visiber(self.locators.Current_Address).send_keys("bjnb jb jhb ")
        self.elemeny_is_visiber(self.locators.Permanent_Address).send_keys("smccsmkcnkas ")
        self.elemeny_is_visiber(self.locators.SUMBIT).click()
        time.sleep(5)

    def check_list_form(self):
        full_name = self.elemenys_are_prisents(self.locators.CTEATE_FULL_NAME).text
        email = self.elemenys_are_prisents(self.locators.CREATE_EMAIL).text
        carret_adres = self.elemenys_are_prisents(self.locators.Current_Address).text
        permanent_adress = self.elemenys_are_prisents(self.locators.CREATE_Permanent_Address).text
        return full_name , email ,carret_adres , permanent_adress





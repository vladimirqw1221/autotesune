from selenium.webdriver.common.by import By


class TextElementsLocators:


    FULL_NAME = (By.CSS_SELECTOR, "input[id= 'userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail'")
    Current_Address = (By.CSS_SELECTOR, "textarea[id= 'currentAddress']")
    Permanent_Address = (By.CSS_SELECTOR, "textarea[id= 'permanentAddress']")
    SUMBIT = (By.XPATH, "//button[@id='submit']")

    CTEATE_FULL_NAME = (By.CSS_SELECTOR, "input[id= 'name']")
    CREATE_EMAIL = (By.CSS_SELECTOR, "input[id='email'")
    CREATE_Current_Address = (By.CSS_SELECTOR, "textarea[id= 'currentAddress']")
    CREATE_Permanent_Address = (By.CSS_SELECTOR, "textarea[id= 'permanentAddress']")
    
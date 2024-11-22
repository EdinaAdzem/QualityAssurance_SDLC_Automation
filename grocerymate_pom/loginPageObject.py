from selenium weimport By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    # Define locators
    EMAIL_FIELD = (By.ID, "email")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Login')]")


    def login(self, email, password):
        email_field = self.driver.find_element(*self.EMAIL_FIELD)
        email_field.send_keys(email)
        password_field = self.driver.find_element(*self.PASSWORD_FIELD)
        password_field.send_keys(password)
        login_button = self.driver.find_element(*self.LOGIN_BUTTON)
        login_button.click()
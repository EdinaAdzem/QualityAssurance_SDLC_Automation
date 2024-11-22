from selenium import webdriver
import time
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage


class GroceryMateTest:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_search_and_login(self):
        #open the url
        self.driver.get("https://grocerymate.com")

        #search for any product
        home_page = HomePage(self.driver)
        home_page.search_for_product("Kiwi")
        time.sleep(2)

        #login
        login_page = LoginPage(self.driver)
        login_page.login("test@example.com", "password123")

        # add checks as assers
        assert "My Account" in self.driver.title

    def close(self):
        self.driver.quit()


#check the tests
if __name__ == "__main__":
    test = GroceryMateTest()
    test.test_search_and_login()
    test.close()

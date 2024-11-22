
class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.search_input = page.locator("input[name='search_product']")
        self.search_button = page.locator("button[type='submit']")

    def search_for_product(self, product_name):
        search_bar = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.SEARCH_BAR)
        )
        search_bar.clear()
        search_bar.send_keys(product_name)
        search_button = self.driver.find_element(*self.SEARCH_BUTTON)
        search_button.click()

    def go_to_cart(self):
        cart_icon = self.page.locator("a[href='/shop']")
        cart_icon.click()

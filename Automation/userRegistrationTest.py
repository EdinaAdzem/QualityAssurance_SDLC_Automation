from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time


@pytest.fixture
def setup_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_user_registration(setup_browser):
    driver = setup_browser
    driver.get('https://www.grocerymate.com/register')

    driver.find_element(By.NAME, 'name').send_keys('John Doe')
    driver.find_element(By.NAME, 'email').send_keys('john.doe@example.com')
    driver.find_element(By.NAME, 'password').send_keys('SecurePassword123')
    driver.find_element(By.NAME, 'confirm_password').send_keys('SecurePassword123')

    driver.find_element(By.ID, 'register_button').click()

    time.sleep(3)

    confirmation_message = driver.find_element(By.CLASS_NAME, 'confirmation-message').text
    assert "Registration successful" in confirmation_message

    assert driver.current_url == 'https://www.grocerymate.com/login'
    print("User successfully registered and redirected to login page.")

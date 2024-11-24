from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://grocerymate.masterschool.com'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

try:
    print("Starting user registration test...")
    signup_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/div[1]'))
    )
    signup_button.click()

    driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div[1]/div/form/input[1]').send_keys('colamityjane@test.com')
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div[1]/div/form/input[2]').send_keys('jane1234')

    register_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div[1]/div/form/button')
    register_button.click()

    shop_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div/div/ul/li[2]/a'))
    )
    shop_button.click()

    # age pop up
    print("Handling age confirmation popup...")
    date_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div/div[2]/div/input'))
    )
    date_input.send_keys("01-01-1981")  #hardcode any

    confirm_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div/div[2]/div/button')
    confirm_button.click()

    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div/div[2]/div[1]/div/div[2]/div[3]/div/div[2]/button'))
    )
    add_to_cart_button.click()

    cart_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/div[3]/svg'))
    )
    cart_icon.click()

    cart_items = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div[1]'))
    )
    assert cart_items is not None
    print("Verified product is present in the cart.")

finally:
    driver.quit()

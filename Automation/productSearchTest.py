from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://grocerymate.masterschool.com'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

try:
    print("running through the user registration to be able to get to the product search step...")
    signup_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/div[1]'))
    )
    signup_button.click()

    driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div[1]/div/form/input[1]').send_keys('colamityjane@test.com')
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div[1]/div/form/input[2]').send_keys('jane1234')

    register_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div[1]/div/form/button')
    register_button.click()

    print("to shop page...")
    shop_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div/div/ul/li[2]/a'))
    )
    shop_button.click()

    print("bypassing the  age confirmation popup...")
    date_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div/div[2]/div/input'))
    )
    date_input.send_keys("01-01-1981")  # Hardcoded date of birth
    confirm_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div/div[2]/div/button')
    confirm_button.click()

    print("product search..")
    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div/div/input'))
    )
    search_input.send_keys("Ginger")  #hardcode any

    product_image = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//img[@src="https://seleniumwebsites.fra1.digitaloceanspaces.com/grocery/Ginger.jpg"]'))
    )

    assert product_image is not None, "Ginger product image not found."
    print("Product search successful. Ginger is displayed.")

finally:
    driver.quit()

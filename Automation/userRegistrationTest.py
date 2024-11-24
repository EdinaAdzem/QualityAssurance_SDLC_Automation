from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://grocerymate.masterschool.com'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

try:

    signup_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/div[1]'))
    )
    signup_button.click()

    driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div[1]/div/form/input[1]').send_keys('colamityjane@test.com')
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div[1]/div/form/input[2]').send_keys('jane1234')

    register_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div[1]/div/form/button')
    register_button.click()

finally:
    driver.quit()

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


s = Service("C:/Users/crenauro/Documents/selenium_training/chromedriver.exe")
driver = webdriver.Chrome(service=s)
url = "https://flipkart.com"
driver.get(url)

driver.find_element(By.XPATH, "//button[@class='_2KpZ6l _2doB4z']").click()

time.sleep(5)

try:
    if driver.find_element(By.XPATH, "//img[@alt='Flipkart']").is_displayed():
        print("displayed")
    else:
        print("error")
except Exception as e:
    print("error in opening")
    print(str(e))


actions = ActionChains(driver)
element = driver.find_element(By.XPATH,"//img[@alt='Electronics']")
actions.move_to_element(element)
actions.perform()
time.sleep(5)

driver.save_screenshot("C:/Users/crenauro/Documents/selenium_training/flipkart_image.png") ##SCREENSHOT

driver.quit()

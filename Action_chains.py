import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By


s = Service("C:/Users/crenauro/Documents/selenium_training/chromedriver.exe")
driver = webdriver.Chrome(service=s)
url = "https://flipkart.com"
driver.get(url)
time.sleep(5)
actions = ActionChains(driver)
driver.find_element(By.XPATH,"//img[@alt='Electronics']")
actions.move_to_element("//img[@alt='Electronics']")
actions.perform()
time.sleep(10)


try:
    if driver.find_element(By.XPATH, "//img[@alt='Electronics']").is_displayed():
        print("displayed")
    else:
        print("error")
except Exception as e:
    print("error in opening")
    print(str(e))
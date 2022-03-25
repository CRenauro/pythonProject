from selenium import webdriver
import time

from selenium.webdriver.chrome.service import Service

s = Service("C:/Users/crenauro/Documents/selenium_training/chromedriver.exe")
driver = webdriver.Chrome(service=s)
from selenium.webdriver.common.by import By

driver.get("https://www.google.com/gmail/about/")
driver.find_element(By.XPATH, "//*[@data-action='sign in']").click()
driver.find_element(By.XPATH, "//input[@aria-label='Email or phone']").send_keys("crjrzgrl@gmail.com")
driver.find_element(By.XPATH, "//span[.='Next']").click()


driver.get("https://www.facebook.com/")
driver.forward()
driver.get("https://www.apple.com/")
driver.back()
driver.find_element(By.XPATH, "//input[@id='email']").send_keys("seashell@mac.com")
driver.find_element(By.XPATH, "//input[@aria-label='Password']").send_keys("6qLyT@BhuW")
driver.find_element(By.XPATH, "//button[.='Log In']").click()

driver.close()
# time.sleep(100)

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

s = Service("C:/Users/crenauro/Documents/selenium_training/chromedriver.exe")
driver = webdriver.Chrome(service=s)

url = "https://demoqa.com/alerts"
driver.get(url)
r = requests.get(url)
response_code = r.status_code

driver.find_element(By.XPATH, "//button[@id='alertButton']").click()
time.sleep(5)
alert = driver.switch_to.alert
alert.accept()
time.sleep(5)
print("hello")

driver.find_element(By.XPATH, "//button[@id='confirmButton']").click()
time.sleep(5)
alert = driver.switch_to.alert
alert.dismiss()
time.sleep(5)
print("hello again")


##AD blocking below - need to use scroll to view

time.sleep(5)
element = driver.find_element(By.XPATH,"//button[@id='promtButton']")
driver.execute_script("arguments[0].scrollIntoView();", element)


driver.find_element(By.XPATH, "//button[@id='promtButton']").click()
time.sleep(5)
alert = driver.switch_to.alert
time.sleep(5)
print(alert.text)
time.sleep(3)
alert.send_keys("Clara")
time.sleep(5)
alert.accept()


time.sleep(10)
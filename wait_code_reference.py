import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

s = Service("D:/Selenium+Python/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(.5)  ##not recommended, this slows site down to half second
url = "https://demoqa.com/alerts"
driver.get(url)
r = requests.get(url)
response_code = r.status_code

driver.maximize_window()

#print(len(handles))

element = driver.find_element(By.XPATH,"//button[@id='promtButton']")
driver.execute_script("arguments[0].scrollIntoView();", element)

time.sleep(15)  ##hard sleep

##explicit wait - timeout until condition is met
w = WebDriverWait(driver, 15)
w.until(expected_conditions.element_to_be_clickable((By.XPATH,
"//button[@id='promtButton']")))
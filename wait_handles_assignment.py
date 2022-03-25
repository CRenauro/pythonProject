import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

s = Service("C:/Users/crenauro/Documents/selenium_training/chromedriver.exe")
driver = webdriver.Chrome(service=s)

url = "https://www.facebook.com/"
driver.get(url)
r = requests.get(url)
response_code = r.status_code
print(response_code)

driver.maximize_window()

driver.find_element(By.XPATH, "//input[@id='email']").send_keys("seashell0524@mac.com")
time.sleep(5)
driver.find_element(By.XPATH, "//input[@aria-label='Password']").send_keys("6qLyX2T@BhuW")
w = WebDriverWait(driver, 15)
w.until(expected_conditions.element_to_be_clickable((By.XPATH,"//button[.='Log In']")))
driver.find_element(By.XPATH, "//button[.='Log In']").click()
driver.implicitly_wait(10)

handles = driver.window_handles
len_handles = len(handles)

for i in range(1, 5):
    driver.switch_to.new_window()

driver.switch_to.window(driver.window_handles[0]) #closes facebook
driver.close()##closes facebook
driver.switch_to.window(driver.window_handles[0]) #switches back to first window



driver.switch_to.window(driver.window_handles[0])
driver.get("https://google.com/")

driver.switch_to.window(driver.window_handles[1])
driver.get("https://pluralsight.com/")

driver.switch_to.window(driver.window_handles[2])
driver.get("https://codeacademy.com/")

driver.switch_to.window(driver.window_handles[3])
driver.get("https://udacity.com/")

print(len(handles))

for i in range(1,6):
    driver.switch_to.window(driver.window_handles[2]) #switches back to codeacademy
    time.sleep(3)


driver.quit()
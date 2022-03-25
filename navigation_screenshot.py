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
time.sleep(5)
driver.maximize_window()
driver.save_screenshot("C:/Users/crenauro/Documents/selenium_training/image.png") ##SCREENSHOT
# driver.close()

##MANUALLY OPEN WINDOWS / add breakpoint here
handles = driver.window_handles

len_handles = len(handles)

for i in range(1, len_handles):
    driver.switch_to.window(handles[i])
    time.sleep(5)
print(len(handles))

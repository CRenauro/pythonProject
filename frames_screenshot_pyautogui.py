import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

import requests
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


import pyautogui

from alerts import element

s = Service("C:/Users/crenauro/Documents/selenium_training/chromedriver.exe")
driver = webdriver.Chrome(service=s)


# driver.implicitly_wait(.5)
# url = "https://demoqa.com/frames"
# driver.get(url)
# time.sleep(5)
#
#
# driver.switch_to.frame("frame1")
# element = driver.find_element(By.XPATH,"//iframe[@srcdoc = '<p>Child Iframe</p>']")
# print("switch to frame")
# driver.switch_to.frame(element)
# frame_heading = driver.find_element(By.XPATH,"//p[(text()='Child Iframe']").text
# print(frame_heading)
# driver.switch_to("frame1")

url = "https://demoqa.com/automation-practice-form"
driver.get(url)
time.sleep(5)
#
pyautogui.press('TAB')
pyautogui.press('TAB')
#
# driver.save_screenshot("C:\Users\crenauro\Documents\selenium_training\my_screenshot.png")
#

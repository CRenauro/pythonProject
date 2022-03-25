from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests

s = Service("C:/Users/crenauro/Documents/selenium_training/chromedriver.exe")
driver = webdriver.Chrome(service=s)

url = "https://gmail.com"
# driver.maximize_window()


driver.get(url)
r = requests.get(url)
response_code = r.status_code
print(r.status_code)

# print(driver.page_source)  #page source
if url in driver.current_url:
    print("url matched")
else:
    print("not matched")
page_source = driver.page_source
if not (response_code == 400 or response_code == 500):
    print("opened successfully")
else:
    print("webpage error")
if "fldLoginUserId" in page_source:
    print("got the element")
else:
    print("unable to catch the element")

print("Wait")
driver.close() #close window
driver.quit()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
s = Service("C:/Users/crenauro/Documents/selenium_training/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://weather.com")
driver.maximize_window()
driver.refresh()
driver.get("https://apple.com")
# driver.back()
# driver.forward()
print(driver.title)
page_title = (driver.title)       #page title Apple

if page_title in "welcome to apple":
    print ("title matched")
else:
    print("title not matched")

driver.close()
driver.quit()




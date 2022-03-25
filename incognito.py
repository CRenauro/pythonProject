from selenium import webdriver
c = webdriver.ChromeOptions()
c.add_argument("--incognito")
driver = webdriver.Chrome(executable_path="C:/Users/crenauro/Documents/selenium_training/chromedriver.exe",options=c)
from selenium.webdriver.common.by import By



driver.get("https://www.google.com/gmail/about/")
driver.find_element(By.XPATH, "//*[@data-action='sign in']").click()
driver.find_element(By.XPATH, "//input[@aria-label='Email or phone']").send_keys("crjrzgrl@gmail.com")
driver.find_element(By.XPATH, "//span[.='Next']").click()
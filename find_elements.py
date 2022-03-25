from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:/Users/crenauro/Documents/selenium_training/chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://facebook.com")
print(driver.current_url)
driver.maximize_window()

# driver.find_element(By.XPATH("//input[@id = 'email']")).send_keys("hello")
# driver.find_element(By.XPATH("//input[@id = 'email']")).click()
# driver.find_element_by_name("email").send_keys("goodbye")
# driver.find_element_by_id("//input[@id = 'email']").click()
driver.find_element_by_xpath("//input[@aria-label= 'Password']").send_keys("cr12345")
# driver.find_element_by_xpath("//button[@name= 'login]").click
#
driver.find_element(By.XPATH, "//input[@id='email']").send_keys("cr@gmail.com")
#
# driver.find_element_by_link_text("Forgot password?").click()

mylist = driver.find_elements_by_xpath("//input")
print(len(mylist))

for i in range (1, len(mylist)):
    print(mylist[1])



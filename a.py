from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.instagram.com/?hl=en")
USERNAME = "clg_memories_9999"
PASSWORD = "shivam@12345"
time.sleep(5)
username = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
# username = driver.find_element_by_name("username")

password = driver.find_element_by_name("password")

username.send_key(USERNAME)
password.send_key(PASSWORD)

time.sleep(2)




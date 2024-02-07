from scraping import create_drive, loginBinus
from time import sleep
# from selenium.webdriver.common.by import By

driver = create_drive()
loginBinus(driver)
# driver.get("http://selenium.dev")
# message = driver.find_element(by=By.ID, value="message")

while True:
    sleep(10000)

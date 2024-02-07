from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from config import emailBNS, passwordBNS
from time import sleep


def loginBinus(driver: webdriver) -> bool:
    statusLogin = True

    driver.get("https://newbinusmaya.binus.ac.id/")

    wait = WebDriverWait(driver, 30)

    loginfmt = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[name=loginfmt]")))
    loginfmt.send_keys(emailBNS)
    driver.find_element(by=By.CSS_SELECTOR, value="#idSIButton9").click()
    del loginfmt

    passwd = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[name=passwd]")))
    passwd.send_keys(passwordBNS)
    driver.find_element(by=By.CSS_SELECTOR, value="#idSIButton9").click()
    del passwd

    # timeWait = 10
    # while timeWait > 0:
    #     passwordError = ""
    #     if 

    #     sleep(2)

    return statusLogin

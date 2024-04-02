from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from application.config.settings import emailBNS, passwordBNS


def loginBinus(driver: webdriver) -> bool:
    statusLogin = True

    driver.get("https://newbinusmaya.binus.ac.id/")

    wait10Sec = WebDriverWait(driver, 10)

    # wait button logout
    try:
        FindElementParam = (By.XPATH, "//button[text()='Logout']")
        ButtonLogout = wait10Sec.until(
            EC.visibility_of_element_located(FindElementParam)
        )
        ButtonLogout.click()
    except TimeoutException:
        pass

    wait15Sec = WebDriverWait(driver, 15)

    try:
        # input email
        loginfmt = wait15Sec.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "[name=loginfmt]")
            )
        )
        loginfmt.send_keys(emailBNS)
        driver.find_element(by=By.CSS_SELECTOR, value="#idSIButton9").click()
        del loginfmt

        # input password
        passwd = wait15Sec.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "[name=passwd]"))
        )
        passwd.send_keys(passwordBNS)
        driver.find_element(by=By.CSS_SELECTOR, value="#idSIButton9").click()
        del passwd

        # Confirm yes
        displayName = wait15Sec.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#displayName")
            )
        )
        driver.find_element(by=By.CSS_SELECTOR, value="#idSIButton9").click()
        del displayName
    except TimeoutException:
        current = driver.current_url
        if not (current.find("/lms/dashboard") != -1):
            statusLogin = False

    del wait10Sec
    del wait15Sec

    return statusLogin

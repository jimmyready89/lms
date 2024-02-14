from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def periodList(driver: webdriver) -> list:
    driver.get("https://newbinusmaya.binus.ac.id/lms/course")

    sleep(3)

    CoursesParam = ".label-filter+div"
    CoursesOptionParam = ".dd__menu-list .dd__option"

    CoursesSelect = driver.find_element(by=By.CSS_SELECTOR,
                                        value=CoursesParam)
    CoursesSelect.click()

    CoursesOptionCount = len(
        driver.find_elements(by=By.CSS_SELECTOR,
                             value=CoursesOptionParam)
    )
    CoursesSelect.click()

    URLList = []
    for OptionNumber in range(CoursesOptionCount):
        Text = ""

        CoursesSelect = driver.find_element(by=By.CSS_SELECTOR,
                                            value=CoursesParam)
        CoursesSelect.click()

        sleep(1)

        CoursesOption = driver.find_elements(by=By.CSS_SELECTOR,
                                             value=CoursesOptionParam)
        Text = CoursesOption[OptionNumber].text
        CoursesOption[OptionNumber].click()

        sleep(1)

        URLList.append({
            "Text": Text,
            "URL": driver.current_url
        })

    return URLList

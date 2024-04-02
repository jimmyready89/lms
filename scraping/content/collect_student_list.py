from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from .utility.people_formting import PeopleFormting


def CollectStudentList(driver: webdriver, CourseURL: str) -> list:
    StudentList = []

    driver.get(f"{CourseURL}/people/students")
    sleep(3)

    SelectParam = ".dd__control"
    SelectElementList = driver.find_elements(by=By.CSS_SELECTOR,
                                             value=SelectParam)
    SelectElement = SelectElementList[1]
    ActionChains(driver)\
        .move_to_element(SelectElement)\
        .click()\
        .perform()

    sleep(0.5)

    OptionParam = ".dd__menu-list > div"
    OptionElementList = driver.find_elements(by=By.CSS_SELECTOR,
                                             value=OptionParam)

    ActionChains(driver)\
        .move_to_element(SelectElement)\
        .click()\
        .perform()

    for OptionNo in range(len(OptionElementList)):
        SelectElementList = driver.find_elements(by=By.CSS_SELECTOR,
                                                 value=SelectParam)
        SelectElement = SelectElementList[1]
        ActionChains(driver)\
            .move_to_element(SelectElement)\
            .click()\
            .perform()

        sleep(0.5)

        OptionElementListTemp = driver.find_elements(by=By.CSS_SELECTOR,
                                                     value=OptionParam)
        ActionChains(driver)\
            .move_to_element(OptionElementListTemp[OptionNo])\
            .click()\
            .perform()

        sleep(2)

        PageHTML = driver.page_source
        PageSoup = BeautifulSoup(PageHTML, 'html.parser')
        StudentList += PeopleFormting(PageSoup, "Student")

    return StudentList

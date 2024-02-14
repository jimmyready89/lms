from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def courseList(driver: webdriver) -> list:
    driver.get("https://newbinusmaya.binus.ac.id/lms/course")

    sleep(3)

    CoursesTypeParam = ".container-fluid .nav-tabs a"
    CoursesTypeElementList = driver.find_elements(by=By.CSS_SELECTOR,
                                                  value=CoursesTypeParam)

    CoursesList = []
    for CoursesType in CoursesTypeElementList:
        CoursesTypeText = CoursesType.text
        CoursesType.click()

        sleep(3)

        CoursesTypeParam = ".container-fluid .c-page-region a"
        CoursesElementList = driver.find_elements(by=By.CSS_SELECTOR,
                                                  value=CoursesTypeParam)

        for Courses in CoursesElementList:
            CoursesText = Courses.text

            CoursesList.append({
                "Name": CoursesText,
                "Type": CoursesTypeText,
                "URL": Courses.get_attribute("href")
            })

    return CoursesList

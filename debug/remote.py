from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

url = "http://localhost:62496"
session_id = "c7089c7532b3721f8558d98978fb8bc3"

options = webdriver.ChromeOptions()
driver = webdriver.Remote(command_executor=url, options=options)
driver.close()
driver.session_id = session_id

driver.get("https://newbinusmaya.binus.ac.id/lms/course/22c043c1-ea61-4e2d-a846-66c04cc63cde/forum")

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

print(CoursesList)

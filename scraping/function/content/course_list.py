from ..browser_connection import BrowserConnection
from time import sleep


def CourseList(browserConnection: BrowserConnection) -> list:
    browser = browserConnection.getBrowser()
    page = browser.contexts[0].pages[-1]
    page.goto("https://newbinusmaya.binus.ac.id/lms/course")

    coursesTypeParam = ".container-fluid .nav-tabs a"
    coursesTypeElementList = page.query_selector_all(coursesTypeParam)

    coursesList = []
    for coursesType in coursesTypeElementList:
        coursesTypeText = coursesType.text_content()
        coursesType.click()

        sleep(1)
        coursesParam = ".container-fluid .c-page-region a"
        coursesElementList = page.query_selector_all(coursesParam)

        for courses in coursesElementList:
            coursesText = courses.text_content()

            coursesList.append({
                "Name": coursesText,
                "Type": coursesTypeText,
                "URL": courses.get_attribute("href").replace("/session", "")
            })

    return coursesList

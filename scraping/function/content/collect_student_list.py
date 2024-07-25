from .utility.people_formting import PeopleFormting
from ..browser_connection import BrowserConnection
from bs4 import BeautifulSoup
from time import sleep


def CollectStudentList(browserConnection: BrowserConnection, CourseURL: str) -> list:
    studentList = []

    browser = browserConnection.getBrowser()
    page = browser.contexts[0].pages[-1]
    page.goto(f"{CourseURL}/people/students")

    sleep(2)

    selectParam = ".dd__control"
    selectElementList = page.query_selector_all(selectParam)

    selectElement = selectElementList[1]
    selectElement.scroll_into_view_if_needed()
    selectElement.click()

    sleep(0.5)

    optionParam = ".dd__menu-list > div"
    optionElementList = page.query_selector_all(optionParam)

    selectElement.scroll_into_view_if_needed()
    selectElement.click()

    for OptionNo in range(len(optionElementList)):
        selectElementList = page.query_selector_all(selectParam)

        selectElement = selectElementList[1]
        selectElement.scroll_into_view_if_needed()
        selectElement.click()

        sleep(0.5)

        optionElementListTemp = page.query_selector_all(optionParam)

        selectElement = optionElementListTemp[OptionNo]
        selectElement.scroll_into_view_if_needed()
        selectElement.click()

        sleep(2)

        pageHTML = page.content()
        pageSoup = BeautifulSoup(pageHTML, 'html.parser')

        studentList += PeopleFormting(pageSoup, "Student")

    return studentList

from .utility.people_formting import PeopleFormting
from ..browser_connection import BrowserConnection
from bs4 import BeautifulSoup
from time import sleep


def CollectLecturersList(browserConnection: BrowserConnection, CourseURL: str) -> list:
    lecturersList = []

    browser = browserConnection.getBrowser()
    page = browser.contexts[0].pages[-1]
    page.goto(f"{CourseURL}/people/lecturers")

    sleep(2)

    pageHTML = page.content()
    pageSoup = BeautifulSoup(pageHTML, 'html.parser')
    lecturersList += PeopleFormting(pageSoup, "Lecturers")

    return lecturersList

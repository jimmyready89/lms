from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from .utility.people_formting import PeopleFormting


def CollectLecturersList(driver: webdriver, CourseURL: str) -> list:
    LecturersList = []

    driver.get(f"{CourseURL}/people/lecturers")

    sleep(3)

    PageHTML = driver.page_source
    PageSoup = BeautifulSoup(PageHTML, 'html.parser')
    LecturersList += PeopleFormting(PageSoup, "Lecturers")

    return LecturersList

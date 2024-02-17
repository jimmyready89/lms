from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep


def CollectGroup(driver: webdriver, CourseURL: str) -> object:
    GroupInformation = {
        "Number" : 0,
        "StudentList" : []
    }

    driver.get(f"{CourseURL}/people/group")

    sleep(3)

    OpenDetailParam = "div.tab-pane.active div.d-flex.align-items-center.pointer svg"
    OpenDetailElement = driver.find_element(by=By.CSS_SELECTOR,
                                                value=OpenDetailParam)
    ActionChains(driver)\
        .move_to_element(OpenDetailElement)\
        .click()\
        .perform()
    
    PageHTML = driver.page_source
    PageSoup = BeautifulSoup(PageHTML, 'html.parser')
    
    TabSoup = PageSoup.find("div", {"class": "tab-pane active"})

    GroupSoup = TabSoup.find("span", {"class": "font-weight-bold"})
    GroupInformation["Number"] = int(GroupSoup.text.replace("Group-", ""))

    PeopleSoupList = TabSoup.find_all("div", {"class": "align-self-start"})
    for PeopleSoup in PeopleSoupList:
        PeopleSoupDetailList = PeopleSoup.find_all("span")

        GroupInformation["StudentList"].append(int(PeopleSoupDetailList[0].text))

    return GroupInformation

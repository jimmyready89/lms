from ..browser_connection import BrowserConnection
from bs4 import BeautifulSoup
from time import sleep


def CollectGroup(browserConnection: BrowserConnection, CourseURL: str) -> list:
    groupInformation = {
        "number": 0,
        "studentList": []
    }

    browser = browserConnection.getBrowser()
    page = browser.contexts[0].pages[-1]
    page.goto(f"{CourseURL}/people/group")

    sleep(2)

    openDetailParam = "div.tab-pane.active div.d-flex.align-items-center.pointer svg"
    openDetailElement = page.locator(openDetailParam)
    openDetailElement.scroll_into_view_if_needed()
    openDetailElement.click()

    pageHTML = page.content()
    pageSoup = BeautifulSoup(pageHTML, 'html.parser')

    tabSoup = pageSoup.find("div", {"class": "tab-pane active"})

    groupSoup = tabSoup.find("span", {"class": "font-weight-bold"})
    groupInformation["number"] = int(groupSoup.text.replace("Group-", ""))

    peopleSoupList = tabSoup.find_all("div", {"class": "align-self-start"})
    for peopleSoup in peopleSoupList:
        peopleSoupDetailList = peopleSoup.find_all("span")

        groupInformation["studentList"].append(int(peopleSoupDetailList[0].text))

    return groupInformation

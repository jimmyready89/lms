from bs4 import BeautifulSoup


def PeopleDetailFormating(peopleSoup, type: str) -> object:
    people = {}

    people["type"] = type
    people["name"] = peopleSoup.find("div", {"class": "text-name"}).text
    try:
        people["programName"] = peopleSoup.find("div", {"class": "program-name"}).text
    except BaseException:
        people["programName"] = ""

    peopleTextIdClassSoup = peopleSoup.find_all("div", {"class": "text-id"})
    people["Id"] = peopleTextIdClassSoup[0].text
    # People["Email"] = PeopleTextIdClassSoup[0].text

    return people


def PeopleFormting(Soup: BeautifulSoup, UserType: str = "") -> list:
    peopleList = []

    peopleTabSoup = Soup.find("div", {"class": "tab-pane active"})
    studentSoupList = peopleTabSoup.find_all("div", {"class": "tiles-item"})
    for studentSoup in studentSoupList:
        People = PeopleDetailFormating(studentSoup, UserType)
        peopleList.append(People)

    return peopleList

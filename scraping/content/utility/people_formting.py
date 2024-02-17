from bs4 import BeautifulSoup


def PeopleDetailFormating(PeopleSoup, Type:str) -> object:
    People = {}

    People["Type"] = Type
    People["Name"] = PeopleSoup.find("div", {"class": "text-name"}).text
    try:
        People["ProgramName"] = PeopleSoup.find("div", {"class": "program-name"}).text
    except:
        People["ProgramName"] = ""

    PeopleTextIdClassSoup =  PeopleSoup.find_all("div", {"class": "text-id"})
    People["Email"] = PeopleTextIdClassSoup[0].text
    People["Id"] = PeopleTextIdClassSoup[1].text

    return People

def PeopleFormting(Soup: BeautifulSoup, UserType:str="") -> list:
    PeopleList = []

    PeopleTabSoup = Soup.find("div", {"class":"tab-pane active"})
    StudentSoupList = PeopleTabSoup.find_all("div", {"class": "tiles-item"})
    for StudentSoup in StudentSoupList:
        People = PeopleDetailFormating(StudentSoup, UserType)
        PeopleList.append(People)

    return PeopleList

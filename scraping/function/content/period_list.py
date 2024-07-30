from ..browser_connection import BrowserConnection
from time import sleep


def PeriodList(browserConnection: BrowserConnection) -> list:
    browser = browserConnection.getBrowser()
    page = browser.contexts[0].pages[-1]
    page.goto("https://newbinusmaya.binus.ac.id/lms/course")

    sleep(2)

    coursesParam = ".label-filter+div"
    coursesOptionParam = ".dd__menu-list .dd__option"

    page.locator(coursesParam).click()
    coursesOptionCount = len(page.query_selector_all(coursesOptionParam))

    URLList = []
    for optionNumber in range(coursesOptionCount):
        text = ""

        if optionNumber > 0:
            page.locator(coursesParam).click()

        sleep(1)

        coursesOption = page.query_selector_all(coursesOptionParam)
        text = coursesOption[optionNumber].text_content()

        coursesOption[optionNumber].click()

        sleep(1)

        URLList.append({
            "Text": text,
            "URL": page.url
        })

    return URLList

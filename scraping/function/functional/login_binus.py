from application.config.settings import emailBNS, passwordBNS
from ..browser_connection import BrowserConnection
from playwright._impl._errors import TimeoutError


def loginBinus(browserConnection: BrowserConnection) -> bool:
    browser = browserConnection.getBrowser()
    context = browser.contexts[0]
    page = context.pages[0]
    page.goto('https://newbinusmaya.binus.ac.id')

    statusLogin = False
    emailForm = True

    try:
        page.wait_for_selector("//button[text()='Logout']", timeout=5000)
        statusLogin = True
    except TimeoutError:
        current = page.url
        if current.find(".binus.ac.id") != -1:
            statusLogin = True

    if statusLogin is False:
        try:
            page.wait_for_selector('text=Pick an account', timeout=5000)
            emailForm = False
            page.locator(f"text={emailBNS}").click()
        except TimeoutError:
            pass

        try:
            if emailForm:
                # Input Email
                page.wait_for_selector("[name=loginfmt]", timeout=5000)

                page.locator("[name=loginfmt]").fill("")
                page.locator("[name=loginfmt]").type(emailBNS)

                page.locator("#idSIButton9").click()

            # Input Password
            page.wait_for_selector("[name=passwd]", timeout=5000)

            page.locator("[name=passwd]").fill("")
            page.locator("[name=passwd]").type(passwordBNS)

            page.locator("#idSIButton9").click()

            page.wait_for_selector('text=Stay signed in?', timeout=5000)
            page.locator("#KmsiCheckboxField").check()
            page.locator("#idSIButton9").click()
        except TimeoutError:
            current = page.url
            if current.find(".binus.ac.id") != -1:
                statusLogin = True

    try:
        page.wait_for_selector("div[role=presentation] .binus-SvgIcon-fontSizeMedium", timeout=7500)
        page.locator("div[role=presentation] .binus-SvgIcon-fontSizeMedium").click()
    except TimeoutError:
        pass

    return statusLogin

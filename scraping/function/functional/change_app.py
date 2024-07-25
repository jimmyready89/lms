from ..browser_connection import BrowserConnection
import time


def ChangeApp(browserConnection: BrowserConnection, targetApp: str) -> bool:
    status = True

    browser = browserConnection.getBrowser()

    originalWindow = None
    pages = browser.contexts[0].pages
    originalPageCount = len(pages)
    originalWindow = pages[-1]

    menuVisible = originalWindow.locator("div[activetab='menu-list']").is_visible()
    menuAppListVisible = originalWindow.locator("div[activetab='main-app-list']").is_visible()
    if not menuVisible and not menuAppListVisible:
        originalWindow.locator("img.launcher").click()

    buttonSemestaAppVisible = originalWindow.locator("p:has-text('Semesta App')").is_visible()
    if buttonSemestaAppVisible:
        originalWindow.locator("p:has-text('Semesta App')").click()

    tryNumber = 3
    while tryNumber > 0:
        try:
            time.sleep(0.5)

            originalWindow.evaluate("""
                () => {
                    const path = "//div[@activetab='main-app-list']//p[text()='""" + targetApp + """']";
                    const button = document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                    button.click();
                }
            """)

            time.sleep(0.5)

            browserConnection.updateBrowserInformation()
            browser = browserConnection.getBrowser()
            pages = browser.contexts[0].pages

            if originalPageCount < len(pages):
                originalWindow.close()
                break

        except Exception:
            pass
        tryNumber -= 1

    return status

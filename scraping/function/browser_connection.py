from playwright.sync_api._generated import Browser, Playwright
import subprocess
import socket
import time


class BrowserConnection:
    browser: Browser = None
    port: int = None

    def __init__(self, playwright: Playwright, port: int):
        tryCount = 10
        self.port = port

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            while True:
                try:
                    s.connect(('localhost', port))
                    break
                except socket.error:
                    if tryCount == 0:
                        break

                    subprocess.Popen([
                        playwright.chromium.executable_path,
                        f"--remote-debugging-port={port}",
                    ])

                    tryCount -= 1
                    time.sleep(1)

        self.playwright = playwright
        self.browser = playwright.chromium.connect_over_cdp(f"http://localhost:{port}")

    def updateBrowserInformation(self):
        self.browser = self.playwright.chromium.connect_over_cdp(f"http://localhost:{self.port}")

    def getBrowser(self) -> Browser:
        return self.browser

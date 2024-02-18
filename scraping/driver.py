from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from application.config.settings import BASE_DIR


def create_drive() -> webdriver:
    service = webdriver.ChromeService()

    profile_dir = f"{BASE_DIR}/profile"

    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument(f"user-data-dir={profile_dir}")

    driver = webdriver.Chrome(
        service=service, options=options)

    url = driver.command_executor._url
    session_id = driver.session_id

    print(url, session_id)

    return driver

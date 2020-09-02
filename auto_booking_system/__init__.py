from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from auto_booking_system.auto_book import main
from auto_booking_system.config import LoginConfig


def user_list_gen():
    for details in LoginConfig.user_list:
        user, pw = details
        yield user, pw


def driver():
    import pathlib

    path = pathlib.Path(__file__).parent.absolute()

    options = Options()
    options.add_argument("--headless")
    options.add_argument("window-size=1920x1080")
    return webdriver.Chrome(f"{path}/../chromedriver", options=options)


if __name__ == "__main__":
    for user, pw in user_list_gen():
        main(user, pw, driver())

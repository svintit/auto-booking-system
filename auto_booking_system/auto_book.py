from time import sleep

from selenium.common.exceptions import (
    ElementNotInteractableException,
    NoSuchElementException,
)

from auto_booking_system.config import LoginConfig, BookConfig
from auto_booking_system.utils import async_no_await


class BookWorkout:
    def __init__(self, driver):
        self.driver = driver

    def run_click(self, xpath):
        self.driver.find_element_by_xpath(xpath).click()
        sleep(0.4)

    def login(self, user, pw):
        config = LoginConfig

        self.driver.get(config.url)
        self.driver.find_element_by_xpath(config.email_xpath).send_keys(user)
        self.driver.find_element_by_xpath(config.pass_xpath).send_keys(pw)
        self.run_click(config.login_button_xpath)

    def book(self):
        config = [
            xpath for var, xpath in vars(BookConfig).items() if not var.startswith("__")
        ]

        try:
            self.driver.get(LoginConfig.url)
            for xpath in config:
                self.run_click(xpath)

            print("Booked successfully!")
        except (ElementNotInteractableException, NoSuchElementException):
            self.book()


@async_no_await
def main(user, pw, driver):
    worker = BookWorkout(driver)
    worker.login(user, pw)
    worker.book()

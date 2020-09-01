from selenium import webdriver

from auto_booking_system.auto_book import main


def driver():
    import pathlib

    path = pathlib.Path(__file__).parent.absolute()

    return webdriver.Chrome(f"{path}/../chromedriver")


if __name__ == "__main__":
    main(driver())

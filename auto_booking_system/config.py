class Config:
    # [(`email`, `password`), (`email`, `password`)]
    user_list = [("**********", "**********")]

    url = "https://myflye.flyefit.ie/myflye/book-workout"


class LoginConfig(Config):
    email_xpath = "/html/body/div[1]/form/div/div/div[2]/div/div[1]/div[2]/input"
    pass_xpath = "/html/body/div[1]/form/div/div/div[2]/div/div[2]/div[2]/input"
    login_button_xpath = "/html/body/div[1]/form/div/div/div[2]/div/div[3]/div[2]/input"


class BookConfig(Config):
    location_button_xpath = "/html/body/div[1]/div[1]/div/section/div[2]/div/form/div/div[2]/div/div/div[2]/span"
    # xpath for the location of the gym below
    location_xpath = "/html/body/div[1]/div[1]/div/section/div[2]/div/form/div/div[2]/div/div/div[3]/div/ul/li[2]"

    date_button_xpath = "/html/body/div[1]/div[1]/div/section/div[2]/div/form/div/div[3]/div/div/div[2]/span"
    # date to book for (usually 24 hours in advance so set to "Tomorrow")
    date_xpath = "/html/body/div[1]/div[1]/div/section/div[2]/div/form/div/div[3]/div/div/div[3]/div/ul/li[2]"

    # time to book for
    book_button_xpath = (
        # Below is 20:30
        # "/html/body/div[1]/div[1]/div/section/div[4]/div/div[11]/a/div[3]/p[2]"
        # Below is 19:00
        "/html/body/div[1]/div[1]/div/section/div[4]/div/div[10]/a/div[3]/p[2]"
    )

    confirm_button_xpath = "/html/body/div[1]/div[2]/div/div/div[3]/a[1]"

import sys
from selene.support.shared import browser
from selenium.webdriver import Keys


def fill_date_of_birthday(date: str):
    name_os = sys.platform
    if name_os == 'darwin':
        browser.element("#dateOfBirthInput").send_keys(Keys.COMMAND + 'a').type(date).press_enter()
    else:
        browser.element("#dateOfBirthInput").send_keys(Keys.CONTROL + 'a').type(date).press_enter()
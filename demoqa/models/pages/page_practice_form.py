import os
from typing import Tuple
from selene import have
from selene.support.shared import browser
from demoqa.models.controls.radio_button import select_radiobutton_gender
from demoqa.models.controls.datepicker import fill_date_of_birthday
from demoqa.models.controls.check_box import select_checkbox
from demoqa.models.controls.dropdown import DropDown
from demoqa.models.data.user import user1
from demoqa.models.controls.line_formatter import subjects_line_formatter


class RegistrationForm:

    def open_page(self, url):
        browser.config.window_width, browser.config.window_height = 1920, 1020
        browser.open_url(url)
        return self

    def fill_first_name(self, first_name: str):
        browser.element("#firstName").type(first_name)
        return self

    def fill_last_name(self, last_name: str):
        browser.element("#lastName").type(last_name)
        return self

    def fill_email(self, email: str):
        browser.element("#userEmail").type(email)
        return self

    def set_gender(self, gender: str):
        select_radiobutton_gender('[for^=gender-radio]', gender)
        return self

    def fill_mobile_phone(self, number_phone: str):
        browser.element('#userNumber').type(number_phone)
        return self

    def set_date_birthday(self, date: str):
        fill_date_of_birthday(date)
        return self

    def fill_subjects(self, subjects: Tuple):
        for subject in subjects:
            browser.element("#subjectsInput").send_keys(subject).press_enter()
        return self
    """
    При добавлении ещё хобби, добавить hoobie2 и hobbie3 в аргументы функции и вызвать select_checkbox для них
    """
    def set_hobbies(self, hobby: str):
        select_checkbox("[for^=hobbies-checkbox]", hobby)
        return self

    def download_file(self, file_name: str):
        browser.element("#uploadPicture").send_keys(os.path.abspath("../resourses/" + file_name))
        return self

    def fill_current_adress(self, adress):
        browser.element("#currentAddress").type(adress)
        return self

    def set_state(self, state):
        state_dropdown = DropDown(browser.element('#state'))
        state_dropdown.select(state)
        return self

    def set_city(self, city):
        state_dropdown = DropDown(browser.element('#city'))
        state_dropdown.select(city)
        return self

    def submit(self):
        browser.element('#submit').press_enter()
        return self

    def check_data(self, value):
        browser.element(".table-responsive").should(have.text(value))
        return self


class RegistrationUser:

    form = RegistrationForm()

    def add_user(self):
        self.form.open_page("https://demoqa.com/automation-practice-form")\
            .fill_first_name(user1.first_name)\
            .fill_last_name(user1.last_name)\
            .fill_email(user1.email)\
            .set_gender(user1.gender)\
            .fill_mobile_phone(user1.number_phone)\
            .set_date_birthday(user1.birthday)\
            .fill_subjects(user1.subjects)\
            .set_hobbies(user1.hobbies)\
            .download_file(user1.file)\
            .fill_current_adress(user1.address)\
            .set_state(user1.state)\
            .set_city(user1.city)\
            .submit()

        self.form.check_data(user1.first_name)\
            .check_data(user1.last_name)\
            .check_data(user1.email)\
            .check_data(user1.gender)\
            .check_data(user1.number_phone)\
            .check_data(user1.birthday) \
            .check_data(subjects_line_formatter(user1.subjects))\
            .check_data(user1.hobbies)\
            .check_data(user1.file)\
            .check_data(user1.address)\
            .check_data(user1.state)\
            .check_data(user1.state)



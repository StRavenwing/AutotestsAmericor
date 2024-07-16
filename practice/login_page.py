import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from .basic_page import BasicPage
from .locators import LoginPageLocators
import time


class LoginPage(BasicPage):

    def __init__(self, *args, **kwargs):
        super(LoginPage, self).__init__(*args, **kwargs)

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.login_form)

    def should_login(self, login, password):
        field_name = self.browser.find_element(*LoginPageLocators.field_name)
        field_password = self.browser.find_element(*LoginPageLocators.field_password)
        login_button = self.browser.find_element(*LoginPageLocators.login_button)
        field_name.clear()
        field_password.clear()
        time.sleep(4)

        field_name.send_keys(login)
        field_password.send_keys(password)
        login_button.click()

    def should_be_code_input(self):
        assert self.is_element_present(*LoginPageLocators.code_input)

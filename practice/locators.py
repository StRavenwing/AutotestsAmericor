from selenium import webdriver

class LoginPageLocators():
    field_name = ('id', 'username')
    field_password = ('name', 'password')
    login_button = ('id', 'login-button')
    login_form = ('id', 'login-form')
    code_input = ('id', 'otp-code')
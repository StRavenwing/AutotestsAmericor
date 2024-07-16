import pytest
from .practice.login_page import LoginPage
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service



test_data = [('demo', 'demo'),
             ('qwe', 'qwe')]


@pytest.mark.parametrize("login,password", test_data)
class TestLogin:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = 'https://idemo.bspb.ru/'
        self.login_page = LoginPage(browser, link)
        self.login_page.open()

    def test_login(self, login, password):
        self.login_page.should_login(login, password)

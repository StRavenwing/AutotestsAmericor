import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def browser(request):
    # user_language = request.config.getoption("--language")
    options = Options()
    # options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    # options.add_argument(f'--lang={user_language}')
    # options.add_argument(f'accept-language={user_language}')

    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=1980,1080')
    options.add_argument('--incognito')
    options.add_argument('--ignore-sertificate-errors')
    options.add_argument('--disable-cache')
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--disable-extensions')
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()
    
    # browser = webdriver.Chrome(options=options)
    # yield browser
    # browser.quit()

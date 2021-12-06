import pytest
from page import Page
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(30)
    
    pytest.page = Page(browser, "https://hotline.ua/")
    try:
        yield browser
    finally:
        browser.quit()
    
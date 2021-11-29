import pytest
import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

@allure.suite("language")
@allure.story("test suit for lab 5")
def test_language_change(browser):
    browser.get("https://hotline.ua/")
    lang = browser.find_element(By.CSS_SELECTOR, "span.active.js-change-language").text
    menu = [elem.text.lower() for elem in browser.find_elements(By.CLASS_NAME, "name")]
    if lang == "укр":
        assert "порівняння" in menu
    else:
        assert "сравнения" in menu
    browser.find_element(By.CSS_SELECTOR, 'span[data-tracking-id=global-13]').click()
    menu = [elem.text.lower() for elem in browser.find_elements(By.CLASS_NAME, "name")]
    if lang == "укр":
        assert "сравнения" in menu
    else:
        assert "порівняння" in menu

@allure.suite("search by product name")
@allure.story("test suit for lab 5")
def test_search_rez_page(browser):
    browser.get("https://hotline.ua/")
    search_term = "sony"
    with allure.step("find " + search_term):
        browser.find_element(By.ID, "searchbox").send_keys(search_term)
        browser.find_element(By.ID, "searchbox").send_keys(Keys.RETURN)
        
    with allure.step("headline check"):
        actual_text = browser.find_element(By.CSS_SELECTOR, "h1.cell-md").text.lower()
        expected_text = search_term
        assert actual_text == expected_text 
    

    
    
        

from selenium.webdriver.common.by import By

class Page:
    def __init__(self, browser, url):
        browser.get("https://hotline.ua/")
        self.browser = browser
        
    def getLang(self, lang):
        return self.browser.find_element(By.CSS_SELECTOR, 'span[data-language='+lang+']')
    
    def getLangActive(self):
        return self.browser.find_element(By.CSS_SELECTOR, "span.active.js-change-language")
    
    def getSearchBox(self):
        return self.browser.find_element(By.ID, "searchbox")
    
    def getHeadline(self):
        return self.browser.find_element(By.CSS_SELECTOR, "h1.cell-md")
    
    def getMenuElements(self):
        return [elem.text.lower() for elem in self.browser.find_elements(By.CLASS_NAME, "name")]
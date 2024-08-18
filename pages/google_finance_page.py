from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class GoogleFinancePage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {"page_title": ("XPATH", "//a[@id='sdgBod']/span[text()='Finance']")}

    def is_title_visible(self):
        try:
            return WebDriverWait(self.driver, 10).until(
                EC.visibility_of(self.page_title)
            )
        except TimeoutException:
            return False

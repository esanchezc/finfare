from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from seleniumpagefactory.Pagefactory import PageFactory


class GoogleFinancePage(PageFactory):
    def __init__(self, driver: webdriver):
        self.driver: driver = driver

    locators = {
        "page_title": ("XPATH", "//a[@id='sdgBod']/span[text()='Finance']"),
        "watchlist_title": ("ID", "smart-watchlist-title"),
        "watchlist_items": (By.CSS_SELECTOR, "#smart-watchlist-title + ul > li"),
        "watchlist_symbol": (By.CSS_SELECTOR, "div.COaKTb"),
    }

    def is_title_visible(self):
        try:
            return WebDriverWait(self.driver, 10).until(
                EC.visibility_of(self.page_title)
            )
        except TimeoutException:
            return False

    def get_watchlist_stock_symbols(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of(self.watchlist_title))

            watchlist_items = self.driver.find_elements(
                *self.locators["watchlist_items"]
            )

            stock_symbols = []
            for item in watchlist_items:
                symbol_element = item.find_element(*self.locators["watchlist_symbol"])
                stock_symbols.append(symbol_element.text.strip())

            return stock_symbols

        except TimeoutException:
            print("Watchlist title not found or timed out")
            return []
        except Exception as e:
            print(f"An error occurred while retrieving stock symbols: {str(e)}")
            return []

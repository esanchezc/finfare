from typing import List

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from seleniumpagefactory.Pagefactory import PageFactory


class GoogleFinancePage(PageFactory):
    def __init__(self, driver: webdriver.Remote):
        self.driver: webdriver.Remote = driver

    locators = {
        "page_title": (By.XPATH, "//a[@id='sdgBod']/span[text()='Finance']"),
        "watchlist_title": (By.ID, "smart-watchlist-title"),
        "watchlist_items": (By.CSS_SELECTOR, "#smart-watchlist-title + ul > li"),
        "watchlist_symbol": (By.CSS_SELECTOR, "div.COaKTb"),
    }

    def is_title_visible(self, timeout: int = 10) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.locators["page_title"])
            )
            return True
        except TimeoutException:
            return False

    def get_watchlist_stock_symbols(self, timeout: int = 10) -> List[str]:
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.locators["watchlist_title"])
            )

            watchlist_items = self.driver.find_elements(
                *self.locators["watchlist_items"]
            )

            stock_symbols = []
            for item in watchlist_items:
                try:
                    symbol_element = item.find_element(
                        *self.locators["watchlist_symbol"]
                    )
                    stock_symbols.append(symbol_element.text.strip())
                except NoSuchElementException:
                    continue  # Skip this item if the symbol element is not found

            return stock_symbols

        except TimeoutException:
            print("Watchlist title not found or timed out")
            return []
        except Exception as e:
            print(f"An error occurred while retrieving stock symbols: {str(e)}")
            return []

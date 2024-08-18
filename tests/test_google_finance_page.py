import pytest

from pages.google_finance_page import GoogleFinancePage


def test_open_google_finance_page(driver):
    finance_page = GoogleFinancePage(driver)
    finance_page.is_title_visible(), "Finance page title is not visible"

def test_get_stock_symbols(driver):
    finance_page = GoogleFinancePage(driver)
    assert len(finance_page.get_watchlist_stock_symbols()) == 6, "Stock symbols not found"
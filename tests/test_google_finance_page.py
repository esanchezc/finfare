import pytest

from pages.google_finance_page import GoogleFinancePage


def test_open_google_finance_page(driver):
    finance_page = GoogleFinancePage(driver)
    finance_page.is_title_visible(), "Finance page title is not visible"
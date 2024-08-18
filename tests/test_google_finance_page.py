import pytest
from pages.google_finance_page import GoogleFinancePage
from config import TestConfig

@pytest.fixture(scope="module")
def finance_page(driver):
    return GoogleFinancePage(driver)

@pytest.fixture(scope="module")
def displayed_symbols(finance_page):
    return finance_page.get_watchlist_stock_symbols()

def test_open_google_finance_page(finance_page):
    assert finance_page.is_title_visible(), "Finance page title is not visible"

def test_should_get_six_stocks_you_may_be_interested_in(displayed_symbols):
    assert len(displayed_symbols) == 6, f"Expected 6 stock symbols, {len(displayed_symbols)} found"

def test_compare_stock_symbols(displayed_symbols):
    found_symbols = set(TestConfig.STOCK_SYMBOLS) & set(displayed_symbols)
    not_in_test_data = set(displayed_symbols) - set(TestConfig.STOCK_SYMBOLS)
    
    print_stock_list("\nStocks you might be interested in that are in the test data:", found_symbols)
    print_stock_list("\nStocks you might be interested that are not in the test data:", not_in_test_data)
    
    assert found_symbols, "None of the expected stock symbols were found in the watchlist"
    print(f"\n{len(found_symbols)} out of {len(TestConfig.STOCK_SYMBOLS)} expected stock symbols were found in the watchlist")

def test_print_test_data_stocks_not_in_interested_stocks(displayed_symbols):
    missing_stocks = set(TestConfig.STOCK_SYMBOLS) - set(displayed_symbols)
    print_stock_list("\nStocks in test data that are not in stocks you might be interested in:", missing_stocks)

def test_print_interested_stocks_not_in_test_data(displayed_symbols):
    missing_stocks = set(displayed_symbols) - set(TestConfig.STOCK_SYMBOLS)
    print_stock_list("\nStocks you might be interested in that are not in test data:", missing_stocks)

def print_stock_list(header, stocks):
    print(header)
    for symbol in stocks:
        print(f"- {symbol}")
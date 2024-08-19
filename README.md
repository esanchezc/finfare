# Google Finance Test Suite

This repository contains an automated test suite for the Google Finance page using Selenium WebDriver with Python. The suite is designed to compare displayed stock symbols with a predefined list.

## Project Structure

```
.
├── config.py
├── conftest.py
├── pages/
│   └── google_finance_page.py
├── tests/
│   └── test_google_finance_page.py
└── README.md
```

## Setup

1. Ensure you have Python 3.12+ installed on your system.
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Configuration

The `config.py` file contains the test configuration:

- `BASE_URL`: The URL of the Google Finance page
- `STOCK_SYMBOLS`: A list of stock symbols to compare against the displayed watchlist

You can modify these values to suit your testing needs.

## Page Object

The `GoogleFinancePage` class in `pages/google_finance_page.py` implements the Page Object pattern for the Google Finance page. It provides methods to interact with and verify elements on the page.

## Test Fixtures

The `conftest.py` file contains pytest fixtures:

- `driver`: Sets up and tears down the WebDriver for each test module
- `finance_page`: Creates an instance of the `GoogleFinancePage`
- `displayed_symbols`: Retrieves the list of displayed stock symbols

## Running Tests

To run the tests, execute the following command in the project root directory:

```
pytest tests/test_google_finance_page.py
```

To run tests with the `print_test` marker:

```
pytest -m print_test tests/test_google_finance_page.py
```

## Test Cases

The test suite includes the following test cases:

1. Verify that the Google Finance page title is visible
2. Check that exactly 6 stock symbols are displayed in the watchlist
3. Compare displayed stock symbols with the predefined list in `TestConfig`
4. Print stocks from test data not found in the watchlist (marked with `print_test`)
5. Print stocks from the watchlist not found in test data (marked with `print_test`)

## Customization

You can modify the `TestConfig` class in `config.py` to change the base URL or the list of stock symbols to compare against.

## GitHub Actions Workflows

This project uses GitHub Actions to automate test execution. There are two workflows defined:

### 1. Nightly Google Finance Test Run

This workflow runs automatically every day at 2:00 AM UTC.

### 2. Manual Google Finance Test Run

This workflow can be triggered manually through the GitHub Actions UI.

This workflow allows you to manually trigger the tests and provides an option to run only the print tests. When triggered, you can choose whether to run all tests or just the print tests marked with the `print_test` marker.

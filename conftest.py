import pytest
from selenium import webdriver

from config import TestConfig


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.get(TestConfig.BASE_URL)
    yield driver
    driver.quit()
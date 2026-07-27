import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import BASE_URL

SEARCH_TERM = "测试"

def test_search_article(driver):
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 10)

    # 等待搜索框可见
    search_input = wait.until(EC.visibility_of_element_located((By.NAME, "s")))
    search_input.send_keys(SEARCH_TERM)
    search_input.submit()

    # 等待搜索结果
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "search-results")))
    assert SEARCH_TERM in driver.page_source
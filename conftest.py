import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options as EdgeOptions

BASE_URL = "http://120.25.77.137"          # 注意：这里是 http 不是 https
ADMIN_USER = "DzChow"
ADMIN_PASS = "&0vyD*!HyaN)FJq7VL"

@pytest.fixture(scope="function")
def driver():
    edge_options = EdgeOptions()
    # 关键：忽略证书错误、禁用安全策略、允许不安全内容
    edge_options.add_argument("--ignore-certificate-errors")
    edge_options.add_argument("--allow-running-insecure-content")
    edge_options.add_argument("--disable-web-security")
    edge_options.add_argument("--disable-features=BlockInsecurePrivateNetworkRequests")
    edge_options.add_argument("--no-sandbox")
    edge_options.add_argument("--disable-dev-shm-usage")

    service = Service(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service, options=edge_options)
    driver.maximize_window()
    yield driver
    driver.quit()
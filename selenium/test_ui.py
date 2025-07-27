
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

driver.get("http://localhost:30007")
assert "DevOps Fullstack App" in driver.page_source

driver.quit()

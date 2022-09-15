from sre_constants import ASSERT
from selenium import webdriver

driver = webdriver.Chrome()

def test_buka_orangehrm():
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    title = driver.title
    assert title == "OrangeHRM"

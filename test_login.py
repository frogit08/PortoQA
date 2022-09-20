from optparse import Option
from pickle import MARK
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


creden = [
    ("admin", "admin"), #Login gagal
    ("Admin", "admin"), #login gagal
    ("asd", "admin123"), #login gagal
    ("admin", "admin123")
]

@pytest.fixture
def setup():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ["enable-logging"])

    driver = webdriver.Chrome(options=options)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.implicitly_wait(10)
    yield driver


@pytest.mark.parametrize('user, passw', creden)
def test_login(setup, user, passw):

    setup.find_element(By.NAME, 'username').send_keys(user)
    setup.find_element(By.NAME, 'password').send_keys(passw)
    setup.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()

    # invalid = driver.find_element(By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']").text
    valid = setup.current_url
    
    if valid == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login":
        assert valid == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    else:
        assert valid == "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList"

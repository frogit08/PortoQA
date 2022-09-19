from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pickle import MARK
import pytest
import pyautogui
import time


@pytest.fixture
def setup():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ["enable-logging"])
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.find_element(By.NAME, 'username').send_keys("Admin")
    driver.find_element(By.NAME, 'password').send_keys("admin123")
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
    yield driver

def test_add_employ(setup):
    setup.find_element(By.LINK_TEXT, 'Add Employee').click()
    setup.find_element(By.NAME, 'firstName').send_keys("Hamzah")
    setup.find_element(By.NAME, 'middleName').send_keys("")
    setup.find_element(By.NAME, 'lastName').send_keys("Padil")
    setup.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]').click()

    #fill
    setup.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div').click()
    pyautogui.press('i',presses=5)
    time.sleep(3)
    setup.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]').click()
    pyautogui.press('s')
    time.sleep(3)
    setup.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input' ).send_keys("1999-10-15")
    setup.find_element(By.XPATH, "//label[normalize-space()='Male']").click()
    setup.find_element(By.XPATH, "//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//button[@type='submit'][normalize-space()='Save']").click()
    teks = WebDriverWait(setup,10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oxd-toaster_1"]'))).text[:7]
    assert teks == "Success"
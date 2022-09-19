"""
custom marker digunakan untuk menjalankan suatu fungsi tertentu dan melewati fungsi yg lain

dijalankan pada terminal dengan code:
pytest nama_file -v -m nama_mark
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pickle import MARK
import pytest



creden = [
    ("admin", "admin"), #Login gagal
    ("Admin", "admin"), #login gagal
    ("asd", "admin123"), #login gagal
]

#=============================================================================================
#   FIXTURE
#=============================================================================================

@pytest.fixture
def setup():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ["enable-logging"])
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.implicitly_wait(10)
    yield driver #fungsinya mengembalikan nilai dan menghentikan sementara eksekusi fungtion yg sedang berjalan
    # driver.close()

#=============================================================================================
#   SCENARIO/TESTCASE 1: LOGIN DENGAN USERNAME ATAU PASSWORD YANG SALAH
#=============================================================================================
@pytest.mark.negativetest #memberikan nama_mark
@pytest.mark.parametrize('user, pasw', creden)
def test_login_negatif(setup,user, pasw):
    setup.find_element(By.NAME, 'username').send_keys(user)
    setup.find_element(By.NAME, 'password').send_keys(pasw)
    setup.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()

    invalid = setup.find_element(By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']").text

    assert invalid == "Invalid credentials"

#=============================================================================================
#   SCENARIO/TESTCASE 2: LOGIN DENGAN USERNAME ATAU PASSWORD YANG BENAR
#=============================================================================================
@pytest.mark.positivetest
def test_login_positif(setup):
    setup.find_element(By.NAME, 'username').send_keys("Admin")
    setup.find_element(By.NAME, 'password').send_keys("admin123")
    setup.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()

    valid = setup.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[1]/span/h6').text

    assert valid == "PIM"

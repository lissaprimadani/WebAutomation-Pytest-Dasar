from _pytest import mark
from _pytest.mark.structures import Mark
from selenium import webdriver
import pytest


Kunci = [
    ("idejongkok","asdgjsddejdn"), #username benar password salah
    ("asdsdwwwwed","asDF12#$"), #username salah password benar
    ("asdfg","asdfg") #username salah password salah
]

driver = webdriver.Chrome()
driver.implicitly_wait(15)

def test_login_success():
    driver.get("https://demoqa.com/login")
    driver.find_element_by_id("userName").send_keys("idejongkok")
    driver.find_element_by_id("password").send_keys("asDF12#$")
    driver.find_element_by_id("login").click()

@pytest.mark.parametrize('a,b', Kunci)
def test_login_failed(a,b):
    driver.get("https://demoqa.com/login")
    driver.find_element_by_id("userName").send_keys(a)
    driver.find_element_by_id("password").send_keys(b)
    driver.find_element_by_id("login").click()

    

    invalidText = driver.find_element_by_id("name").text
    
    assert invalidText == "Invalid username or password!"

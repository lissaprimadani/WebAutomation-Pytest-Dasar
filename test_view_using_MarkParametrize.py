from selenium import webdriver
import pytest
driver = webdriver.Chrome()

Alamat = [
    ("https://www.instagram.com","Instagram"),
    ("https://www.facebook.com","Facebook – log in or sign up")
]

@pytest.mark.parametrize('address,result',Alamat)
def test_bukaAlamat(address,result):
    driver.get(address)
    Title = driver.title
    assert Title == result
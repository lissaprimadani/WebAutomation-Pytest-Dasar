from selenium import webdriver

driver = webdriver.Chrome()

def test_bukaGoogle():
    driver.get("https://www.google.com")
    Title = driver.title
    assert Title == "Google"


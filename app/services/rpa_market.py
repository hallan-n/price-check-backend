from selenium.webdriver import Firefox
from pydantic import BaseModel as BM
from app.models.login import Login
from selenium.webdriver.common.by import By


def run(value: Login):
    browser = Firefox()
    USER = "hallansantos2017@gmail.com"
    PASS = "Hallan@123"
    URL = "https://www.magazineluiza.com.br/"
    browser.get(URL)
    browser.implicitly_wait(3)
    login_button = browser.find_element(By.XPATH, "//a[@class='sc-uVWWZ hEcWif sc-kpKSZj dZQCuD sc-kpKSZj dZQCuD']")
    login_button.click()
    browser.implicitly_wait(6)
    input_user = browser.find_elements(By.NAME, "login")
    input_pass = browser.find_element(By.NAME, "password")
    input_user[1].send_keys(USER)
    input_pass.send_keys(PASS)
    button_logar = browser.find_element(By.ID, "login-box-form-continue")
    button_logar.click()
    browser.implicitly_wait(3)
    print(login_button)

    return True




from selenium.webdriver import Firefox
from pydantic import BaseModel as BM
from app.models.login import Login
from app.models.product import Product
from app.models.store import Store
from selenium.webdriver.common.by import By


def run(product: Product, store: Store, login: Login):
    browser = Firefox()
    USER = login.username
    PASS = login.password
    URL = store.store_url
    URL_PRODUCT = product.product_url

    if "magazine" in store.store_name.lower():
        browser.get(URL)
        browser.implicitly_wait(3)
        login_button = browser.find_element(
            By.XPATH, "//a[@class='sc-uVWWZ hEcWif sc-kpKSZj dZQCuD sc-kpKSZj dZQCuD']"
        )
        login_button.click()
        browser.implicitly_wait(6)
        input_user = browser.find_elements(By.NAME, "login")
        input_pass = browser.find_element(By.NAME, "password")
        input_user[1].send_keys(USER)
        input_pass.send_keys(PASS)
        button_logar = browser.find_element(By.ID, "login-box-form-continue")
        button_logar.click()
        browser.implicitly_wait(10)
        try:
            resp = browser.find_element(
                By.XPATH,
                "//p[contains(@id, 'aria-login')]|//div[@class='LoginBox-form-error--unique']",
            )
            if resp:
                return {"resp": "Login ou senha incorretos"}
        except:
            browser.get(URL_PRODUCT)
            browser.implicitly_wait(10)
            button_bag = browser.find_elements(
                By.XPATH, "//div[@class='sc-dhKdcB kbCiGN']//button"
            )
            button_bag[1].click()
            return {"resp": "Produto adicionado ao carrinho com sucesso!"}
    if "havan" in store.store_name.lower():
        browser.get(URL)
        browser.implicitly_wait(5)
        login_button_side = browser.find_element(By.ID, "sidebarCollapse-button")
        login_button_side.click()
        browser.implicitly_wait(5)
        login_button_side = browser.find_element(By.ID, "amgdprcookie-button -allow -save")
        login_button_side.click()
        browser.implicitly_wait(5)
        login_button = browser.find_element(By.XPATH, "//div[contains(@class, 'navigation-account-link')]//a")
        browser.implicitly_wait(5)
        login_button.click()
        browser.implicitly_wait(5)
        input_user = browser.find_element(By.XPATH, "//div[contains(@class,'field email')]/input")
        browser.implicitly_wait(5)
        input_user.send_keys(USER)
        browser.implicitly_wait(5)
        input_pass.send_keys(PASS)
        browser.implicitly_wait(5)
        input_pass = browser.find_element(By.CLASS_NAME, "button-submit")
        browser.implicitly_wait(5)
        input_pass.click()
        browser.implicitly_wait(5)
        browser.get(URL_PRODUCT)
        browser.implicitly_wait(5)
        add_car = browser.find_element(By.ID, "pickupstore-button")
        add_car.click()
        browser.implicitly_wait(5)

    browser.quit()


from selenium.webdriver.common.by import By
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
def test_add_to_basket_button_is_present(browser):
    browser.get(link)
    try:
        button = browser.find_element(By.CSS_SELECTOR, '#add_to_basket_form button')
    except NoSuchElementException:
        assert False, "Button is not found"
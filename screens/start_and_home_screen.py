import time

from helpers.common_helpers import *
from web_driver.driver import *
from locators.flipkart_locators import *


def select_language(driver):
    is_visible(driver, SELECT_LANGUAGE, 30)
    do_click(driver, SELECT_LANGUAGE)
    is_visible(driver, CONTINUE_BTN, 10)
    do_click(driver, CONTINUE_BTN)
    is_visible(driver, CLOSE_BTN, 30)
    do_click(driver, CLOSE_BTN)


def search_on_home_screen(driver):
    is_visible(driver, SEARCH_BAR, 30)
    do_click(driver, SEARCH_BAR)
    is_visible(driver, SEARCH, 15)
    do_send_keys(driver, SEARCH, 'Iphone 13', 10)
    do_click(driver, FIRST_SEARCH_RESULT, 15)
    time.sleep(4)

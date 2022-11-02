from helpers.common_helpers import *
from web_driver.driver import *
from locators.flipkart_locators import *


def select_a_product(driver):
    # scroll the screen to find product
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("APPLE iPhone 11 (Black, 128 GB)").instance(0));')
    is_visible(driver, IPHONE_11, 10)
    do_click(driver, IPHONE_11)


def add_to_cart(driver):
    is_visible(driver, ADD_TO_CART, 15)
    do_click(driver, ADD_TO_CART)
    go_to_cart = is_visible(driver, GO_TO_CART, 20)
    assert go_to_cart is True

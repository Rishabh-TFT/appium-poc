from screens.products_screens import *
from screens.start_and_home_screen import *
from pytest_bdd import given, when, then


@given('I select English Language')
def select_eng_lang(driver):
    select_language(driver)


@when('I search products')
def search_products(driver):
    search_on_home_screen(driver)


@then('I select a product')
def select_product(driver):
    select_a_product(driver)


@then('I verify product added to cart')
def add_product(driver):
    add_to_cart(driver)

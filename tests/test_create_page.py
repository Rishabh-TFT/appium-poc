from pytest_bdd import when, then
from selenium.common.exceptions import WebDriverException
from pages.create_page import *
from pages.editor_page import *


@when('I search the video')
def video_search(browser):
    try:
        search_video(browser, "christmas")
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, video_search)


@when('I search the video new user')
def video_search_new_user(browser):
    try:
        search_video(browser, "christmas")
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, video_search_new_user)


@when('I am filtering premium videos on create page')
def verify_premium_media(browser):
    try:
        filter_premium_media(browser, "love")
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, verify_premium_media)


@when('I am filtering editorial videos and photos on create page')
def verify_editorial_media(browser):
    try:
        filter_editorial_media_photos(browser, "love")
        filter_editorial_media(browser, "love")
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, verify_editorial_media)


@when('I verify sorting')
def check_sorting(browser):
    try:
        verify_sorting(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, check_sorting)


@when('I fully preview a video')
def full_preview_of_video(browser):
    try:
        preview_and_verify_preview_functionalities_template(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, full_preview_of_video)


@allure.severity(allure.severity_level.NORMAL)
@when('I customize the video')
def customize_template(browser):
    try:
        customize_chosen_template(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, customize_template)


@allure.severity(allure.severity_level.NORMAL)
@when('I goto Drafts page')
def goto_draft_dashboard(browser):
    try:
        goto_draft_page(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, goto_draft_dashboard)


@then('I go to create page')
def goto_create_page(browser):
    try:
        go_to_create_page(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, goto_create_page)


# Upload -  Photos
@when('I am uploading a photo on create page')
def upload_a_photo_create_page(browser):
    try:
        upload_photo_on_create_page(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, upload_a_photo_create_page)
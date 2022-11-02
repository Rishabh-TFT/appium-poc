import time
from selenium.common.exceptions import ElementNotInteractableException, ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
from helpers.common_helpers import *
from test_data.testdata import *
from locators.locators_file import *
from pages.new_login_page import skip_cookies

ir_google_events = []
ir_mixpanel_events = []


def analytics_cookie(browser):
    """
    Args:
        browser:
    Perform: Activate analytics using cookie
    """
    browser.add_cookie({'name': 'analyticDebug', 'value': 'true'})
    browser.refresh()
    time.sleep(2)


def navigate_image_resizer_page(browser):
    """
    Navigates to Image resizer page
    """
    is_visible(browser, TOOLS_BTN)
    do_hover(browser, TOOLS_BTN)
    do_click(browser, IMAGE_RESIZER_BTN)
    time.sleep(3)
    title = browser.title
    assert title == title_image_resizer
    skip_cookies(browser)


def upload_ir(browser):
    """
    Args:
        browser:
    Perform: Upload image file in Image Resizer tool
    """
    elem = browser.find_element(IR_UPLOAD_PATH[0], IR_UPLOAD_PATH[1])
    elem.send_keys(os.getcwd() + upload_photo)
    assert is_visible(browser, IR_IMAGE_UPLOADED_BOX, 20) is True


def change_ir_width_height(browser):
    """
    Args:
        browser:
    Perform: Change Uploaded image width and height Image Resizer tool
    """
    is_visible(browser, IR_RATIO_CHECKBOX)
    do_click(browser, IR_RATIO_CHECKBOX)
    is_visible(browser, IR_WIDTH_TXT)
    do_clear(browser, IR_WIDTH_TXT)
    do_send_keys(browser, IR_WIDTH_TXT, '1600')
    is_visible(browser, IR_HEIGHT_TXT)
    do_clear(browser, IR_HEIGHT_TXT)
    do_send_keys(browser, IR_HEIGHT_TXT, '900')


def ir_download_to_login(browser):
    """
    Args:
        browser:
    Perform: Download Uploaded image and assert Promo AD pop up
    """
    is_visible(browser, IR_DOWNLOAD_BUTTON)
    try:
        do_click(browser, IR_DOWNLOAD_BUTTON)
    except ElementClickInterceptedException:
        download_button = browser.find_element(IR_DOWNLOAD_BUTTON[0], IR_DOWNLOAD_BUTTON[1])
        browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", download_button)
        do_click(browser, IR_DOWNLOAD_BUTTON)
    assert is_visible(browser, PROMO_IR_SIGN_UP_POPUP) is True
    google_events = google_analytics(browser)
    mix_events = mixpanel_analytics(browser)
    for ige in google_events:
        ir_google_events.append(ige)
    for ime in mix_events:
        ir_mixpanel_events.append(ime)
    do_click(browser, IR_LOGIN)
    WebDriverWait(browser, 20).until(lambda x: login_title in browser.title)
    title = browser.title
    assert title == login_title
    browser.back()
    if is_visible(browser, PROMO_IR_SIGN_UP_POPUP_CLS, 15) is True:
        do_click(browser, PROMO_IR_SIGN_UP_POPUP_CLS)
    assert is_visible(browser, IR_IMG_PRESENT) is True
    google_events = google_analytics(browser)
    mix_events = mixpanel_analytics(browser)
    for ige in google_events:
        ir_google_events.append(ige)
    for ime in mix_events:
        ir_mixpanel_events.append(ime)


def ir_download_without_login(browser):
    """
    Args:
        browser:
    Perform: Download Uploaded image and assert Promo AD pop up
    """
    is_visible(browser, IR_DOWNLOAD_BUTTON)
    try:
        do_click(browser, IR_DOWNLOAD_BUTTON)
    except ElementClickInterceptedException:
        download_button = browser.find_element(IR_DOWNLOAD_BUTTON[0], IR_DOWNLOAD_BUTTON[1])
        browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", download_button)
        do_click(browser, IR_DOWNLOAD_BUTTON)
    assert is_visible(browser, PROMO_IR_SIGN_UP_POPUP) is True
    google_events = google_analytics(browser)
    mix_events = mixpanel_analytics(browser)
    for ige in google_events:
        ir_google_events.append(ige)
    for ime in mix_events:
        ir_mixpanel_events.append(ime)
    do_click(browser, IR_SIGN_UP)


def select_diff_social_ratios(browser):
    """
    Args:
        browser:
    Perform: Verify different social aspect ratio and download
    """
    for num, social in zip(range(1, 4), ('Facebook', 'Instagram', 'YouTube')):
        do_click(browser, (By.XPATH, IR_SIDE_ICONS[1] + str([num])))
        time.sleep(2)
        do_click(browser, (By.XPATH, f'(//DIV[@data-social="{social}"])[5]//div[2]'))
        elem = browser.find_element(By.XPATH, f'(//DIV[@data-social="{social}"])[5]')
        ratio_selected = "selected" in elem.get_attribute("class")
        assert ratio_selected is True
    is_visible(browser, IR_DOWNLOAD_SELECTED_BUTTON)
    do_click(browser, IR_DOWNLOAD_SELECTED_BUTTON)


def convert_it_image_to_video(browser):
    """
    Args:
        browser:
    Perform: Check analytics events and convert to video
    """
    google_events = google_analytics(browser)
    mix_events = mixpanel_analytics(browser)
    for ige in google_events:
        ir_google_events.append(ige)
    for ime in mix_events:
        ir_mixpanel_events.append(ime)
    elem = browser.find_element(IR_CONVERT_TO_VIDEO_BTN[0], IR_CONVERT_TO_VIDEO_BTN[1])
    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", elem)
    do_click(browser, IR_CONVERT_TO_VIDEO_BTN)
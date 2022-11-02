import os
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, TimeoutException, \
    NoSuchWindowException, ElementClickInterceptedException, WebDriverException, InvalidArgumentException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def do_click(driver, by_locator: object, sec=10):
    """
    Waits and clicks on the chosen element
    Args:
        driver: webdriver
        by_locator (str): chosen locator from locators/locators_file.py
        sec (int): default time to wait
    """
   
    try:
        WebDriverWait(driver, sec, poll_frequency=0.4).until(
            EC.element_to_be_clickable(by_locator)).click()
    except AttributeError as e:
        if str(e) == "'dict' object has no attribute 'is_displayed'":
            raise NoSuchElementException
        else:
            raise e


def do_double_click(driver, by_locator, sec=5):
    """
    Args:
        driver: webdriver
        by_locator (str): chosen locator from locators/locators_file.py
        sec (int): default time to wait
    """
   
    try:
        elem = WebDriverWait(driver, sec, poll_frequency=0.4).until(
            EC.presence_of_element_located(by_locator))
        driver.execute_script("var evt = document.createEvent('MouseEvents');" +
        "evt.initMouseEvent('dblclick',true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0,null);" +
        "arguments[0].dispatchEvent(evt);", elem)
    except AttributeError as e:
        if str(e) == "'dict' object has no attribute 'is_displayed'":
            raise NoSuchElementException
        else:
            raise e


def do_hover(driver, by_locator, sec=5):
    """
    Hovers over element
    Args:
        driver: webdriver
        by_locator (str): chosen locator from locators/locators_file.py
        sec (int): default time to wait
    """
   
    try:
        elem = WebDriverWait(driver, sec, poll_frequency=0.4).until(
            EC.presence_of_element_located(by_locator))
        ActionChains(driver).move_to_element(elem).perform()
    except AttributeError as e:
        if str(e) == "move_to requires a WebElement":
            raise NoSuchElementException
        else:
            raise e


def drag_and_drop(driver, by_locator_source, by_locator_target, sec=5):
    """
    Drag and drop from source to targeted element
    Args:
        driver: webdriver
        by_locator_source (str): chosen source locator from locators/locators_file.py
        by_locator_target (str): chosen target locator from locators/locators_file.py
        sec (int): default time to wait
    """
   
    source = WebDriverWait(driver, sec).until(
        EC.visibility_of_element_located(by_locator_source))
    target = WebDriverWait(driver, sec).until(
        EC.visibility_of_element_located(by_locator_target))
    action = ActionChains(driver)
    action.drag_and_drop(source, target).perform()


def do_send_keys(driver, by_locator, text, sec=5):
    """
    Sends keys to the chosen element
    Args:
        driver: webdriver
        by_locator (str): chosen locator from locators/locators_file.py
        text (str): text to be send
        sec (int): default time to wait
    """
   
    try:
        WebDriverWait(driver, sec, poll_frequency=0.4).until(
            EC.visibility_of_element_located(by_locator)).send_keys(text)
    except AttributeError as e:
        if str(e) == "'dict' object has no attribute 'is_displayed'":
            raise NoSuchElementException
        else:
            raise e


def get_element_text(driver, by_locator: object):
    """
    Gets text of the chosen element
    Args:
        driver: webdriver
        by_locator (str): chosen locator from locators/locators_file.py
    """
   
    try:
        elem_text = WebDriverWait(driver, 30, poll_frequency=0.4).until(
            EC.presence_of_element_located(by_locator)).text
        return elem_text
    except AttributeError as e:
        if str(e) == "'dict' object has no attribute 'is_displayed'":
            raise NoSuchElementException
        elif str(e) == "'dict' object has no attribute 'is_displayed'":
            raise NoSuchElementException
        else:
            raise e


def get_css_value(driver, by_locator, property_name):
    """
    Gets text of the chosen element
    Args:
        property_name: add css property name
        driver: webdriver
        by_locator (str): chosen locator from locators/locators_file.py
    """
   
    try:
        elem = WebDriverWait(driver, 30, poll_frequency=0.4).until(
            EC.presence_of_element_located(by_locator))
        elem_value = elem.value_of_css_property(property_name)
        return elem_value
    except AttributeError as e:
        if str(e) == "'dict' object has no attribute 'is_displayed'":
            raise NoSuchElementException
        elif str(e) == "'dict' object has no attribute 'is_displayed'":
            raise NoSuchElementException
        else:
            raise e


def is_visible(driver, by_locator, sec=5) -> bool:
    """
    Waits and checks if element is visible
    Args:
        driver: webdriver
        by_locator (str): chosen locator from locators/locators_file.py
        sec (int): default time to wait
    Returns:
        True or False
    """
    elem = False
    try:
        elem = WebDriverWait(driver, sec, poll_frequency=0.4, ignored_exceptions=WebDriverException).until(EC.visibility_of_element_located(by_locator))
    except (WebDriverException, Exception, TimeoutException):
        return bool(elem)
    return bool(elem)


def is_invisible(driver, by_locator, sec=5) -> bool:
    """
    Waits and checks if element is invisible
    Args:
        driver: webdriver
        by_locator (str): chosen locator from locators/locators_file.py
        sec (int): default time to wait
    Returns:
        True or False
    """
   
    elem = False
    try:
        elem = WebDriverWait(driver, sec, poll_frequency=0.4, ignored_exceptions=WebDriverException).until(EC.invisibility_of_element_located(by_locator))
    except (WebDriverException, Exception):
        return bool(elem)
    return bool(elem)


def is_clickable(driver, by_locator, sec=5) -> bool:
    """
    Waits and checks if element is clickable
    Args:
        driver: webdriver
        by_locator (str): chosen locator from locators/locators_file.py
        sec (int): default time to wait
    Returns:
        True or False
    """
   
    elem = False
    try:
        elem = WebDriverWait(driver, sec, poll_frequency=0.4).until(EC.element_to_be_clickable(by_locator))
    except (TimeoutException, NoSuchElementException, AttributeError):
        return bool(elem)
    return bool(elem)


def switch_to_iframe(driver, by_locator, sec=10):
    """
    Switches to the chosen iframe
    Args:
        driver: webdriver
        by_locator (str): chosen locator from locators/locators_file.py
        sec (int): default time to wait
    """
    try:
        WebDriverWait(driver, sec, poll_frequency=0.4).until(EC.frame_to_be_available_and_switch_to_it(by_locator))
    except InvalidArgumentException as e:
        if ("Message: invalid argument: missing 'ELEMENT'" in str(e)) is True:
            raise NoSuchElementException
        else:
            raise e


def do_clear(driver, by_locator, sec=5):
    """
    Clears textfield or input
    Args:
        driver: webdriver
        by_locator (str): chosen locator from locators/locators_file.py
        sec (int): default time to wait
    """
   
    try:
        WebDriverWait(driver, sec, poll_frequency=0.4).until(EC.visibility_of_element_located(by_locator)).clear()
    except AttributeError as e:
        if str(e) == "'dict' object has no attribute 'is_displayed'":
            raise NoSuchElementException
        else:
            raise e


def read_creds(file_dir: str, line_num: int) -> str:
    """
    Reads credential information from the file
    Args:
        file_dir (str): path to the file
        line_num (int): line number we want to use
    Returns:
        Credentials (str)
    """
    f = open(os.getcwd() + file_dir, "r")
    read = f.readlines()
    return read[line_num]


def read_creds_chars(file_dir: str, line_num: int, char_num: int) -> str:
    """
    Reads credential information and characters from the file
    Args:
        line_num (int): line number we want to use
        char_num(int): char number we want to use
        file_dir (str): path to the file
    Returns:
        Credentials (str)
    """
    f = open(os.getcwd() + file_dir, "r")
    read = f.readlines()
    read_char = read[line_num]
    return read_char[char_num]







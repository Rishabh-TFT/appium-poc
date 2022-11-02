import os
import pdb
from appium import webdriver
import pytest
from web_driver.config import *


@pytest.fixture()
def driver():
    """
    Configures driver parameters - local device or remote
    Use when calling pytest
    """
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
    driver.implicitly_wait(30)
    yield driver
    driver.quit()



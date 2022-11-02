from pytest_bdd import scenarios
from web_driver.driver import driver
from tests.test_flipkart_automation import *
import pytest

scenarios('feature_files/test_flipkart_automation.feature')
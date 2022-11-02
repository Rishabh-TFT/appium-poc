from pytest_bdd import scenarios

from web_driver.driver import browser, mob_browser

from tests.test_create_page import *
from tests.test_editor_page import *

from tests.test_dashboard import *

from tests.test_flipkart_automation import  *
import pytest


scenarios('feature_files/test_local_scenarios.feature')
scenarios('feature_files/test_flipkart_automation.feature')
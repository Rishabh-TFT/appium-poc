from appium.webdriver.common.appiumby import AppiumBy

SELECT_LANGUAGE = (AppiumBy.XPATH,  "//android.widget.TextView[@text='English']")
CONTINUE_BTN = (AppiumBy.XPATH,  "//android.widget.Button[@text='CONTINUE']")
CLOSE_BTN = (AppiumBy.ID, "custom_back_icon")
SEARCH_BAR = (AppiumBy.ID, "com.flipkart.android:id/search_widget_textbox")
SEARCH = (AppiumBy.ID, "com.flipkart.android:id/search_autoCompleteTextView")
FIRST_SEARCH_RESULT = (AppiumBy.XPATH, "//android.widget.LinearLayout[1]")
IPHONE_11 = (AppiumBy.XPATH, "//android.widget.TextView[@text='APPLE iPhone 11 (Black, 128 GB)']")
ADD_TO_CART = (AppiumBy.XPATH, "//android.widget.TextView[@text='ADD TO CART']")
GO_TO_CART = (AppiumBy.XPATH, "//android.widget.TextView[@text='GO TO CART']")


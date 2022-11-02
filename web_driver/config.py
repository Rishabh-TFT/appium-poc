import os

desired_cap = {
    # Set URL of the application under test
    "app": os.getcwd() + "/files/com.flipkart.android.1150200.apk",
    "platformVersion": "13",
    "platformName": "Android",
    "deviceName": "Pixel 6 Pro",
    "appPackage": "",
    "appWaitActivity": "",
    'newCommandTimeout': 200000,
    'deviceReadyTimeout': 2000,
    'autoDissmissAlerts': True,
    'autoGrantPermissions': True
}
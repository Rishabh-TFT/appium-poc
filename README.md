# appium-poc
# Automation Script for flipkart.com

Technology stack: [Python](https://www.python.org/), [appium](https://appium.io//), 
[PyTest](https://docs.pytest.org/en/stable/), [PyTest BDD](https://pypi.org/project/pytest-bdd/)

### Directory structure
├── assets                                              # local folder contained credentials
├── feature_files                                       # folder contains Gherkin scenarios 
├── files                                               # folder contains android apk files 
├── locators                                            # folder contains locators    
├── screens                                             # folder contains functions to be used in the test steps   
├── test_data                                           # folder contains test data urls, titles, message and sample user email accounts
├── tests                                               # folder contains Gherkin steps for scenarios
├── web_driver                                          # folder contains webdriver and appium configurations 
├── conftest.py                                         # the file contains code related to Slack reports
├── requirements.txt                                    # pip requirements file


## Local environment setup 

To use this project Python 3.10. is required.

Windows
```bash
python3.10 -m venv venv
\path\to\env\Scripts\activate
example: C:\Users\Username\venv\Scripts\activate.bat
pip install pip-tools
pip install -r requirements.txt

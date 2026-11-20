import json, pytest, os
import time
from pathlib import Path

from pageObjects.login import *
from pageObjects.dashboard import *
from utils.apiBaseFramework import *

#Read JSON
BASE_DIR = Path(__file__).resolve().parent
data_file_path = os.path.join(BASE_DIR,"data","credentials.json")

with open(data_file_path) as f:
    test_data = json.load(f)
    print(test_data)
    user_credentials_list = test_data['user_credentials']

@pytest.mark.smoke
@pytest.mark.parametrize( 'user_credentials', user_credentials_list)
def test_e2e_web_api(playwright:Playwright, browserInstance, user_credentials):

    try:
        userEmail = user_credentials['userEmail']
        userPassword = user_credentials['userPassword']

        # created object and sending page variable to loginPage class in login.py file present in pageObjects directory
        login_Page = LoginPage(browserInstance)

        # created object and sending page variable to loginPage class in login.py file present in pageObjects directory
        accessDashboardObjects = DashboardPage(browserInstance)

        login_Page.navigateToURL() # called the method from loginPage class in login.py method
        time.sleep(3)
        # Create order and get orderID
        api_utils = APIUtils() # imported apiBase.py file and calling APIUtils class
        orderId = api_utils.createOrder(playwright, user_credentials) # calling and storing returned value of createorder() method
                                                    # from APIUtils class

        # sending email and password extracted from JSON file to the method present in login.py file
        login_Page.input_user_credentials(userEmail, userPassword)

        # Dashboard page -> access method in dashboard.py file to click on Orders button on Dashboard
        # caught the returned variable from dashboard.py file in ordersHistoryPage variable
        ordersHistoryPage = accessDashboardObjects.selectOrdersNavLink()

        # used the value caught in ordersHistoryPage variable and used it to call selectAndViewOrder method from ordersHistory.py file
        # caught the returned value from ordersHistory.py file for orderDetailsPage method in orderDetails.py file
        orderDetailsPage = ordersHistoryPage.selectAndViewOrder(orderId)
        orderDetailsPage.verifyThanksText()

    except Exception as ex:
        print(f"Failed because {ex}")
        raise
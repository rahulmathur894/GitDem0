from pytest_bdd import given, when, then, parsers, scenarios
import pytest

from pageObjects.login import *
from utils.apiBaseFramework import *

scenarios('features/orderTransaction.feature')

@pytest.fixture()
# created this empty dictionary to store and move the data between different functions within this file
def shared_data():
    return {}

@given (parsers.parse('Open the browser, navigate to URL and login with {username} and {password}'))
# to catch the username and password values sent by feature file, we need to use curly brace to give variables in @given section
def place_item_order(playwright:Playwright, username, password, shared_data):
    api_utils = APIUtils()  # imported apiBase.py file and calling APIUtils class
    # create a runtime dictionary to send as an argument with variable user_credentials
    # this is needed here as we have already setup the data previously
    user_credentials = {}
    user_credentials['userEmail'] = username
    user_credentials['userPassword'] = password
    orderId = api_utils.createOrder(playwright, user_credentials)
    shared_data['order_id']=orderId # stored order id value in dictionary declared in fixture
    shared_data['user_name']=username
    shared_data['user_password']=password


@given ('the user is on landing page')

def user_on_landing_page(browserInstance, shared_data):
    # created object and sending page variable to loginPage class in login.py file present in pageObjects directory
    login_Page = LoginPage(browserInstance)
    login_Page.navigateToURL() # called the method from loginPage class in login.py method
    shared_data['login_Page'] = login_Page # key-value pair
    user_name = shared_data['user_name'] # used declared dictionary fixture values here from def place_item_order function above
    user_password = shared_data['user_password']

    dashboardPage = login_Page.input_user_credentials(user_name, user_password)

    shared_data['dashboard_page'] = dashboardPage
    print("dashboard_page:", shared_data.get('dashboard_page'))


@when ('I click on Orders menu option')

def go_to_orders_page(shared_data):

    accessDashboardOjects = shared_data['dashboard_page']
    ordersHistoryPage = accessDashboardOjects.selectOrdersNavLink()
    shared_data['ordersHistory_page'] = ordersHistoryPage


@when ('Orders page is displayed, select the orderID')

def select_order_id(shared_data):
    ordersHistoryPage = shared_data['ordersHistory_page']
    orderId= shared_data['order_id']
    orderDetailsPage = ordersHistoryPage.selectAndViewOrder(orderId)
    shared_data['order_details_page'] = orderDetailsPage


@then ('Check the order success message is displayed')

def verify_success_message(shared_data):
    orderDetailsPage = shared_data['order_details_page']
    orderDetailsPage.verifyThanksText()

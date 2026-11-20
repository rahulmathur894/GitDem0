from playwright.sync_api import expect, Playwright, Page
from utils.apiBase import *

def test_e2e_web_api(playwright:Playwright):

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client")

    # Create order and get orderID
    api_utils = APIUtils() # imported apiBase.py file and calling APIUtils class
    orderId = api_utils.createOrder(playwright) # calling and storing returned value of createorder() method
                                                # from APIUtils class


    # Login
    # login id: rahulmathur@gmail.com Password: Rahul@123
    page.get_by_placeholder("email@example.com").fill("rahulmathur@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Rahul@123")
    page.get_by_role("button", name="Login").click()


    # Order History Page -> Verify order is present
    page.get_by_role("button", name="ORDERS").click()

    orderIdRow = page.locator("tr").filter(has_text=orderId) # use the value of order id object
    orderIdRow.get_by_role("button", name="View").click()

    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")

    context.close()
    browser.close()


def test_Github_print_test():
    print("Codeline 1")
    print("Codeline 2")

    print("Codeline 3")

def test_Github_branchCreate_test():
    print("Codeline 1")

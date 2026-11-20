import time
from playwright.sync_api import Page, expect, Playwright
from utils.apiBase import APIUtils


# continue_() method is used to send an intercepted network request directly to the network
def interceptRequest(route):
    route.continue_(url="https://rahulshettyacademy.com/client/#/dashboard/order-details/6ac6054e2be7a4bc2b90d117")


def test_Network_2(page:Page):

    page.goto("https://rahulshettyacademy.com/client")
    # used '*' as order id can be different everytime
    # route method is used to listen to the network. Get all the information about that API call
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", interceptRequest)
    page.get_by_placeholder("email@example.com").fill("rahulmathur@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Rahul@123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    #time.sleep(60)
    invalidAuthorizationMessage = page.locator(".blink_me").text_content()
    print(invalidAuthorizationMessage)
    expect(page.locator(".blink_me")).to_contain_text("You are not authorize to view this order")


# Injecting token directly in session local storage to skip login (session storage)

def test_session_storage(playwright:Playwright, page:Page):
    api_utils = APIUtils()
    token = api_utils.getToken(playwright)

    # script to inject token in session local storage
    # script should be in triple quotes, and in javascript, any javascript initialization should happen in triple quotes
    #add_init_script() means add initialization script method is used to access local storage and inject the token value

    page.add_init_script(f"""localStorage.setItem("token", '{token}')""")

    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name="Orders").click()
    #expect(page.locator("h1")).to_contain_text("Your Orders")
    expect(page.get_by_text("Your Orders")).to_be_visible()

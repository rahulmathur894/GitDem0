import pytest
from playwright.sync_api import Page, expect

# -> make API call from brower -> api call contact server return back response to browser -> broweser use response to generate html

fakePayloadResponse = {"data":[],"message":"No Orders"}

def intercept_response(route): # route parameter gets the data from page.route used in test function

    # when the server returns back with response, instead of fulfilling actual response, fake it by giving the fake payload response
    route.fulfill(
        json = fakePayloadResponse
    )

@pytest.mark.smoke
def test_Network_1(page: Page):

    page.goto("https://rahulshettyacademy.com/client")
    # used '*' as members id can be different everytime
    # route method is used to listen to the network. Get all the information about that API call
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    page.get_by_placeholder("email@example.com").fill("rahulmathur@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Rahul@123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    noOrderMessage = page.locator(".mt-4").text_content()
    print(noOrderMessage)
    expect(page.locator(".mt-4")).to_contain_text(" You have No Orders to show at this time.")

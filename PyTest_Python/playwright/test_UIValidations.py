import time
from playwright.sync_api import Page, expect, Playwright

def test_UIValidationDynamicScript(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()

    # locating object with tag name
    # multiple tags are present of same name, so filtering with filter method
    iphoneProduct = page.locator("app-card").filter(has_text="iphone X")

    # as we have stored the filtered object in variable, we can use that variable to work with filtered object
    iphoneProduct.get_by_role("button", name="Add").click()

    nokiaProduct = page.locator("app-card").filter(has_text="Nokia Edge")
    nokiaProduct.get_by_role("button", name="Add").click()

    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)

def test_childWindowHandle(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    # listener function called to access new page opened in new tab

    with page.expect_popup() as childPage_info:
        page.locator(".blinkingText").filter(has_text="Free Access").click()

        # storing value of childPage_info object in childPage variable so that we can work on the page objects

        childPage = childPage_info.value

        #storing entire text string of the webpage object in a variable

        #verifyText = childPage.locator(".red").text_content()
        verifyText = childPage.locator(".im-para").filter(has_text="Please email us at ").text_content()
        print(verifyText)

        #Please email us at mentor@rahulshettyacademy.com with below template to receive response

        #split the string in two parts

        words = verifyText.split("at")
        
        # split more to get the email separately

        email = words[1].strip().split(" ")[0]

        # verify that the email is correct

        assert email == 'mentor@rahulshettyacademy.com'


        #time.sleep(2)

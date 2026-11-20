import time

from playwright.sync_api import Page, expect

def test_moreUIValidations(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    # get by placeholder locator
    # hide, display assertion of the objects and locating with placeholder
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()


    # Alert Boxes

    page.on("dialog", lambda dialog:dialog.accept())# anonymous functions can be used with keyword lambda
    page.get_by_role("button", name="Confirm").click()
    #time.sleep(4)


    # Mouse Hover

    page.locator("#mousehover").hover()
    page.get_by_role("link", name="Top").click()


    # Frame Handling

    pageFrame = page.frame_locator("#courses-iframe")
    pageFrame.get_by_role("link", name="All Access plan").click()
    expect(pageFrame.locator("body")).to_contain_text("Happy Subscibers")


    # Testing Table Components and Data

    # Questions: Check the Price of Rice is equal 37
    # identify the Price column
    # identify the Rice row
    # extract the price of the rice

    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count() > 0:
            priceColValue = index
            break

    riceRow = page.locator("tr").filter(has_text = "Rice")

    expect(riceRow.locator("td").nth(priceColValue)).to_have_text("37")


# Codegen example

#Write playwright codegen <URL> of application in the terminal
# - Stop the recording and verify the recorded steps

def test_codegenEx(page: Page):

    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/")
    page.get_by_role("button", name="ADD TO CART").first.click()
    page.get_by_role("button", name="ADD TO CART").first.click()
    page.get_by_role("button", name="ADD TO CART").nth(5).click()
    page.locator("div:nth-child(10) > .product-action > button").click()
    page.locator("div:nth-child(16) > .product-action > button").click()
    page.locator("div:nth-child(22) > .product-action > button").click()
    page.locator("div:nth-child(30) > .product-action > button").click()
    page.get_by_role("link", name="Cart").click()
    page.get_by_role("button", name="PROCEED TO CHECKOUT").click()
    page.get_by_role("textbox", name="Enter promo code").click()
    page.get_by_role("textbox", name="Enter promo code").fill("No")
    page.locator("div").nth(5).click()
    page.get_by_role("button", name="Apply").click()
    page.get_by_role("button", name="Place Order").click()
    page.get_by_role("combobox").select_option("India")
    page.get_by_role("checkbox").check()
    page.get_by_role("button", name="Proceed").click()
import time, pytest
from playwright.sync_api import Page, expect, Playwright  # importing Page, expect class to get methods suggestions

@pytest.mark.regression
def test_playwrightBasics(playwright): # playwright fixture comes with pytest-playwright plugin installed
    browser = playwright.chromium.launch(headless=False) # invoke chromium, it supports Chrome and Edge
    context = browser.new_context() # this invoke new browser
    page = context.new_page() # page object created
    page.goto("https://www.rahulshettyacademy.com") # hit the URL

# playwright browser shortcut, chromium headless mode, 1 single context

def test_playwrightShortcut(page:Page): # page object coming from Page class of playwright.sync_api package
    page.goto("https://www.rahulshettyacademy.com")


# UI elements automation example

def test_coreLocators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy") # get object with label named Username:
    page.get_by_label("Password:").fill("Learning@830$3mK200")
    page.get_by_role("combobox").select_option("teach")
    # get object by role if only 1 object is there, not successful if multiple objects are there of same type
    page.locator("#terms").check() # CSS locator # for id and . for class
    page.get_by_role("link", name="terms and conditions").click() # locating by name
    page.get_by_role("button", name="Sign In").click()
    # get object with generic term combobox for dropdowns,
    # select_option will have value present in value attribute of option tag and not the real text of the option

    #Assertion - Verify if this test is displayed when inputting wrong credentials:
    #Incorrect username/password.

    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()

    time.sleep(10)


# running tests in Firefox

def test_firefoxBrowser(playwright:Playwright):
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
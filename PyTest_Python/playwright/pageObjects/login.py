# Write the methods which belongs to Login page
import time
from playwright.sync_api import Page
from pageObjects.dashboard import DashboardPage


class LoginPage:

    def __init__(self, page):
        self.page = page

        # locator of captcha image
        self.captcha_image = page.locator("#cpBodyMain_cpBody_ssoCaptcha_imgCaptcha")

        # locator of captcha image text input
        self.captcha_input = page.locator("#cpBodyMain_cpBody_ssoCaptcha_txtCaptcha")

    def navigateToURL(self):
        self.page.goto("https://rahulshettyacademy.com/client")
        time.sleep(5)

    def input_user_credentials(self, userEmail, userPassword):
        self.page.get_by_placeholder("email@example.com").fill(userEmail)
        self.page.get_by_placeholder("enter your passsword").fill(userPassword)
        self.page.get_by_role("button", name="Login").click()
        dashboardPage = DashboardPage(self.page)
        return dashboardPage

    def captcha_webpage_open(self):
        self.page.goto("https://sso.rajasthan.gov.in/signin")

    def get_captcha_image(self):
        return self.captcha_image

    def get_captcha_screenshot(self):
        return self.captcha_image.screenshot()
# Real Time Example for captcha
from pageObjects import login
from utils.Captcha_OCR import CaptchaOCR

from playwright.sync_api import Page, expect
import time, ddddocr, io

def test_captcha_betterCode_govtSite(page:Page, playwright):

    ocr = ddddocr.DdddOcr(show_ad=False)

    ocr.set_ranges("abcdefghijklmnopqrstuvwxyz@!#$%^&*()_+={}[]:;'|\<,>.?/`~1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    # object created
    loginPage = login.LoginPage(page)

    loginPage.captcha_webpage_open()

    assert loginPage.get_captcha_image().is_visible()

    page.wait_for_timeout(500)

    image = loginPage.get_captcha_screenshot()

    ocr = CaptchaOCR()
    text = ocr.read_captcha(image)

    loginPage.captcha_input.fill(text)

    time.sleep(3)
    print(f"extracted_text: {text}")
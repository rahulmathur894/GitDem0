from PIL import Image, ImageEnhance
from playwright.sync_api import Page, expect
from playwright_recaptcha import recaptchav2
import time, ddddocr, io

# image text captchas
def test_captcha_ddddocr(page:Page, playwright):

    ocr = ddddocr.DdddOcr()

    page.goto("https://solvecaptcha.com/demo/image-captcha")

    captcha_element=page.get_by_alt_text("image captcha")

    image_bytes = captcha_element.screenshot()

    ocr.set_ranges("abcdefghijklmnopqrstuvwxyz@!#$%^&*()_+={}[]:;'|\<,>.?/`~1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    extracted_text = ocr.classification(image_bytes)

    page.locator("#ts-box").fill(extracted_text.upper())

    time.sleep(3)

    page.get_by_role("button", name="Check").click()

    try:
        expect(page.get_by_text("Captcha is passed successfully!")).to_be_visible()
        print("Correct captcha")
    except Exception as e:
        expect(page.get_by_text("Captcha solved incorrectly, please try again.")).to_be_visible()
        print("Wrong captcha")

    time.sleep(3)

    print(f"extracted_text: {extracted_text}")



# reCAPTCHA

def test_GooglereCaptcha(page:Page, playwright):

    page.goto("https://google.com/recaptcha/api2/demo")

    page.wait_for_timeout(3000)

    with recaptchav2.SyncSolver(page) as solver:
        solver.solve_recaptcha(wait=True)

    print("Captcha solved successfully")

    page.locator("#recaptcha-demo-submit").click()

    try:

        expect(page.locator(".recaptcha-success")).to_be_visible()

    except Exception as e:

        print(e)




# Real Time Example for captcha

def test_captcha_betterCode_govtSite(page:Page, playwright):

    ocr = ddddocr.DdddOcr(show_ad=False)

    page.goto("https://sso.rajasthan.gov.in/signin")

    captcha_element=page.locator("#cpBodyMain_cpBody_ssoCaptcha_imgCaptcha")

    page.wait_for_timeout(500)

    image_bytes = captcha_element.screenshot()

    ocr.set_ranges("abcdefghijklmnopqrstuvwxyz@!#$%^&*()_+={}[]:;'|\<,>.?/`~1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    # Preprocess the image
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

    # Enlarge the image while preserving its aspect ratio
    image = image.resize(
        (image.width * 10, image.height * 10),
        Image.Resampling.LANCZOS
    )

    # Improve contrast slightly
    image = ImageEnhance.Contrast(image).enhance(1.5)

    # Convert the processed image back to bytes
    output = io.BytesIO()
    image.save(output, format="PNG")
    processed_bytes = output.getvalue()

    extracted_text = ocr.classification(processed_bytes).strip()

    page.locator("#cpBodyMain_cpBody_ssoCaptcha_txtCaptcha").fill(extracted_text)

    time.sleep(3)
    print(f"extracted_text: {extracted_text}")

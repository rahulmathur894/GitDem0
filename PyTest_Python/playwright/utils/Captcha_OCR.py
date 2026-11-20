import ddddocr, io
from PIL import Image, ImageEnhance, ImageFilter

class CaptchaOCR:

    def __init__(self):
        self.ocr = ddddocr.DdddOcr(show_ad=False)

    def read_captcha(self, image_bytes):

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

        extracted_text = self.ocr.classification(processed_bytes).strip()

        return extracted_text

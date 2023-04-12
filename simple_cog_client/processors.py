import io
from base64 import b64encode, b64decode

from PIL import Image

class ImageProcessor:    
    def encode(self, img_path):
        buffer = io.BytesIO()
        img = Image.open(img_path).convert("RGB")
        img.save(buffer, format="PNG")
        return b64encode(buffer.getvalue()).decode('utf-8')
    def decode(self, img_str):
        img_bytes = b64decode(img_str)
        img = Image.open(io.BytesIO(img_bytes))
        return img


class OCRExtractionsProcessor:
    def encode(self, extractions):
        raise NotImplementedError
    
    def decode(self, extractions):
        return extractions


processors = {
    "image": ImageProcessor(),
    "ocr_extractions": OCRExtractionsProcessor(),
}

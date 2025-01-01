import json
from pathlib import Path
from config.settings import GOOGLE_API_KEY, USE_GPU
from utils.logger import setup_logger
from utils.ocr import OCRExtractor
from utils.prompt import create_prompt
from services.genai_service import GenerativeAIService

logger = setup_logger()

class ReceiptParser:
    def __init__(self, google_api_key, use_gpu):
        self.ocr = OCRExtractor(use_gpu=use_gpu)
        self.genai = GenerativeAIService(api_key=google_api_key)

    def parse_receipt(self, image_path):
        if not Path(image_path).exists():
            raise FileNotFoundError(f"Image not found: {image_path}")
        ocr_text = self.ocr.extract_text(image_path)
        if not ocr_text:
            return None
        prompt = create_prompt(ocr_text)
        return json.loads(self.genai.parse_receipt_text(prompt))

if __name__ == "__main__":
    try:
        parser = ReceiptParser(GOOGLE_API_KEY, USE_GPU)
        result = parser.parse_receipt("data/sample/nota3.png")
        print(json.dumps(result, indent=2) if result else "Failed to parse receipt")
    except Exception as e:
        logger.error(f"Error: {e}")

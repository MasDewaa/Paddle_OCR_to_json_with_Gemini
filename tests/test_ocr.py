import unittest
from utils.ocr import OCRExtractor

class TestOCRExtractor(unittest.TestCase):
    def setUp(self):
        self.ocr = OCRExtractor(use_gpu=False)

    def test_extract_text_valid_image(self):
        # Replace 'sample_receipt.png' with a real test image path.
        image_path = 'data/sample/nota3.png'
        text = self.ocr.extract_text(image_path)
        self.assertTrue(isinstance(text, str) and len(text) > 0, "OCR should return non-empty text.")

    def test_extract_text_invalid_image(self):
        with self.assertRaises(FileNotFoundError):
            self.ocr.extract_text("invalid_path.png")

if __name__ == "__main__":
    unittest.main()

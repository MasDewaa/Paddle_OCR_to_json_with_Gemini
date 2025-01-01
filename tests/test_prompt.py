import unittest
from main import ReceiptParser
from config.settings import GOOGLE_API_KEY

class TestReceiptParser(unittest.TestCase):
    def setUp(self):
        self.parser = ReceiptParser(google_api_key=GOOGLE_API_KEY, use_gpu=False)

    def test_parse_receipt_valid_image(self):
        # Replace 'sample_receipt.png' with a real test image path.
        image_path = 'data/sample/nota3.png'
        result = self.parser.parse_receipt(image_path)
        self.assertTrue(isinstance(result, dict), "Result should be a dictionary.")
        self.assertIn("store", result, "JSON result should contain 'store' key.")
        self.assertIn("items", result, "JSON result should contain 'items' key.")

    def test_parse_receipt_invalid_image(self):
        with self.assertRaises(FileNotFoundError):
            self.parser.parse_receipt("invalid_path.png")

if __name__ == "__main__":
    unittest.main()

import unittest
from utils.prompt import create_prompt

class TestPromptCreation(unittest.TestCase):
    def test_create_prompt(self):
        ocr_text = "Sample store\nDate: 2023-12-31\nItem1 10.00\nTotal: 20.00"
        prompt = create_prompt(ocr_text)
        self.assertIn("Parse the following receipt text into JSON:", prompt, "Prompt should contain instruction.")
        self.assertIn(ocr_text, prompt, "Prompt should include the OCR text.")
        self.assertIn("Format:", prompt, "Prompt should specify the JSON format.")

if __name__ == "__main__":
    unittest.main()

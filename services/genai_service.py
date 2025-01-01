import google.generativeai as genai

class GenerativeAIService:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def parse_receipt_text(self, prompt):
        response = self.model.generate_content(
            prompt,
            generation_config=genai.GenerationConfig(temperature=0.1, response_mime_type="application/json")
        )
        return response.text

def create_prompt(ocr_text):
    """
    Create a prompt for parsing receipt text into JSON.
    :param ocr_text: The extracted OCR text.
    :return: A string containing the prompt for the generative model.
    """
    return f"""
        Parse the following receipt text into JSON:
        {ocr_text}
        Format: {{store: string, date: string, items: [{{item_name: string, category: string, quantity: int, subprice: int, price: int}}], total: int}}
        Correction item names and assign categories. Use null if uncertain.
        """

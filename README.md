# Receipt Parser Project

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Testing](#testing)

## Introduction
The **Receipt Parser Project** is a Python-based application designed to extract information from receipt images and convert it into structured JSON format. It uses Optical Character Recognition (OCR) for text extraction and integrates with Google's Generative AI to parse and structure the extracted text.

## Features
- **OCR Integration:** Utilizes PaddleOCR to extract text from receipt images.
- **Text Parsing:** Converts extracted text into structured JSON format with keys like `store`, `date`, `items`, and `total`.
- **Category Assignment:** Automatically categorizes receipt items based on text.
- **Modular Design:** Highly maintainable and testable codebase.

## Technologies Used
- **Python:** Programming language.
- **PaddleOCR:** For Optical Character Recognition.
- **Google Generative AI:** To parse receipt text into JSON.
- **unittest:** For testing individual modules.

## Project Structure
```
/
|
├── main.py               # Entry point for the application
├── config/
│   └── settings.py       # Configuration for API keys and environment
├── utils/
│   ├── ocr.py            # OCR utility
│   ├── prompt.py         # Prompt generation utility
│   └── logger.py         # Logging utility
├── services/
│   └── genai_service.py  # Integration with Google Generative AI
└── tests/
    ├── test_ocr.py       # Unit tests for OCR functionality
    ├── test_prompt.py    # Unit tests for prompt generation
    └── test_parser.py    # Unit tests for the receipt parser
```

## Setup Instructions
### Prerequisites
- Python 3.8 or later
- Pipenv or virtualenv for dependency management

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/receipt-parser.git
   cd receipt-parser
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your API key in `config/settings.py`:
   ```python
   GOOGLE_API_KEY = "your_google_api_key_here"
   ```

## Usage
1. Place your receipt image in the root directory.
2. Run the application:
   ```bash
   python main.py
   ```
3. The parsed JSON will be printed to the console or saved as required.

## Testing
Run unit tests to verify the functionality of individual modules:
```bash
python -m unittest discover -s tests
```

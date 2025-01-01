from paddleocr import PaddleOCR

class OCRExtractor:
    """
    A class to handle Optical Character Recognition (OCR) using PaddleOCR.
    """

    def __init__(self, use_gpu=True):
        """
        Initialize the OCRExtractor.
        :param use_gpu: Whether to use GPU for OCR processing.
        """
        self.ocr = PaddleOCR(use_angle_cls=True, lang='id', show_log=False, use_gpu=use_gpu, enable_mkldnn=True)

    def extract_text(self, image_path):
        """
        Extract text from an image using PaddleOCR.
        :param image_path: Path to the image file.
        :return: Extracted text as a string.
        :raises FileNotFoundError: If the image file does not exist.
        """
        if not Path(image_path).exists():
            raise FileNotFoundError(f"Image not found: {image_path}")
        result = self.ocr.ocr(image_path, cls=True)
        return "\n".join(line[1][0] for line in result[0] if len(line) >= 2 and isinstance(line[1], tuple))
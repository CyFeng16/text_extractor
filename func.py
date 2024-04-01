from pathlib import Path
from typing import Union, Dict, List, Any

from paddleocr import PaddleOCR

# Create OCR instance at the global level to avoid reinitializing it multiple times.
OCR_INSTANCE = PaddleOCR(use_angle_cls=True, lang="ch", ocr_version="PP-OCRv4")


def extract_text(image_path: Union[str, Path]) -> Dict[str, Union[str, List[Any]]]:
    """
    Extracts text from an image using PaddleOCR.

    Args:
        image_path (Union[str, Path]): The path to the image file.

    Returns:
        Dict[str, Union[str, List[Any]]]: A dictionary containing the status,
                                           extracted text messages, and pure text.
    """
    # Convert Path to str if necessary
    if isinstance(image_path, Path):
        image_path = str(image_path)

    try:
        results = OCR_INSTANCE.ocr(image_path, cls=True)

        result_dict = {"status": "success", "messages": [], "pure_text": []}

        for item in results[0]:
            bounding_box, (text, confidence) = item[0], item[1]

            result_item = {
                "text": text,
                "confidence": confidence,
                "boundingBox": bounding_box,
            }
            result_dict["messages"].append(result_item)
            result_dict["pure_text"].append(text)
    except Exception as e:
        result_dict = {"status": "error", "messages": str(e), "pure_text": []}

    return result_dict

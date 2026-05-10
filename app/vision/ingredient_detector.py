"""
Person 1 module: Computer Vision / Ingredient Detection

Replace the demo logic with real OpenCV, YOLO, TensorFlow, or PyTorch detection.
The function must return a list of ingredient names.
"""

from typing import List


def detect_ingredients(image_path: str) -> List[str]:
    """
    Detect ingredients from uploaded image.

    Args:
        image_path: Path to uploaded image.

    Returns:
        List of detected ingredient names.
    """

    # TODO: Replace this demo list with real computer vision detection.
    # Example future logic:
    # 1. Load image with OpenCV
    # 2. Run YOLO/object detection model
    # 3. Convert detected labels to ingredient names
    # 4. Return unique ingredients

    demo_ingredients = ["tomato", "egg", "cheese", "onion"]
    return demo_ingredients

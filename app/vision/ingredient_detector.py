import base64
import os
from typing import List

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def encode_image(image_path: str) -> str:
    """
    Convert image to base64 string.
    """

    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def fallback_ingredients() -> List[str]:
    """
    Fallback ingredients if AI detection fails.
    """

    return [
        "tomato",
        "onion",
        "potato",
        "garlic"
    ]


def detect_ingredients(image_path: str) -> List[str]:
    """
    Detect ingredients using OpenAI Vision.
    """

    try:
        base64_image = encode_image(image_path)

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": (
                                "Identify only food ingredients visible in this image. "
                                "Return ONLY a comma separated list."
                            ),
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            },
                        },
                    ],
                }
            ],
            max_tokens=100,
        )

        text_response = response.choices[0].message.content

        ingredients = [
            item.strip().lower()
            for item in text_response.split(",")
            if item.strip()
        ]

        if not ingredients:
            return fallback_ingredients()

        return ingredients

    except Exception as e:
        print(f"\nIngredient Detection Error: {e}")

        return fallback_ingredients()
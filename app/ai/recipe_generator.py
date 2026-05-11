import json
import os
from typing import List, Dict

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_recipes(ingredients: List[str]) -> List[Dict[str, object]]:
    """
    Generate realistic meal suggestions using detected ingredients.
    """

    if not ingredients:
        return []

    prompt = f"""
    You are an AI cooking assistant.

    Detected ingredients:
    {", ".join(ingredients)}

    Generate 4 different meals the user can cook using these ingredients.

    Return ONLY valid JSON in this exact format:
    [
      {{
        "name": "Recipe name",
        "ingredients": ["ingredient1", "ingredient2"],
        "time": "25 minutes",
        "difficulty": "Easy",
        "calories": "350 kcal",
        "steps": ["step 1", "step 2", "step 3"]
      }}
    ]
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=800,
    )

    text_response = response.choices[0].message.content

    try:
        recipes = json.loads(text_response)
    except json.JSONDecodeError:
        recipes = [
            {
                "name": "AI Generated Mixed Meal",
                "ingredients": ingredients,
                "time": "25 minutes",
                "difficulty": "Easy",
                "calories": "350 kcal",
                "steps": [
                    "Wash and prepare all ingredients.",
                    "Chop vegetables into small pieces.",
                    "Cook ingredients in a pan with oil.",
                    "Season and serve warm."
                ]
            }
        ]

    return recipes
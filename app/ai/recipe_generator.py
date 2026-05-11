import json
import os
from typing import List, Dict

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def fallback_recipe(ingredients: List[str]) -> List[Dict[str, object]]:
    """
    Emergency fallback recipes if AI response fails.
    """

    return [
        {
            "name": "Mixed Vegetable Meal",
            "ingredients": ingredients,
            "time": "25 minutes",
            "difficulty": "Easy",
            "calories": "350 kcal",
            "steps": [
                "Wash all vegetables carefully.",
                "Chop ingredients into small pieces.",
                "Heat olive oil in a pan.",
                "Cook vegetables until soft.",
                "Season and serve warm."
            ]
        }
    ]


def generate_recipes(ingredients: List[str]) -> List[Dict[str, object]]:
    """
    Generate AI-powered recipes from detected ingredients.
    """

    if not ingredients:
        return fallback_recipe(ingredients)

    prompt = f"""
    You are a professional AI cooking assistant.

    Available ingredients:
    {", ".join(ingredients)}

    Generate 4 realistic meals using these ingredients.

    IMPORTANT:
    - Return ONLY valid JSON
    - No markdown
    - No explanations
    - No extra text

    JSON format:
    [
      {{
        "name": "Recipe name",
        "ingredients": ["ingredient1", "ingredient2"],
        "time": "25 minutes",
        "difficulty": "Easy",
        "calories": "350 kcal",
        "steps": [
          "Step 1",
          "Step 2",
          "Step 3"
        ]
      }}
    ]
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1200,
        )

        text_response = response.choices[0].message.content.strip()

        recipes = json.loads(text_response)

        if not isinstance(recipes, list):
            return fallback_recipe(ingredients)

        return recipes

    except Exception as e:
        print(f"\nAI Recipe Generation Error: {e}")

        return fallback_recipe(ingredients)
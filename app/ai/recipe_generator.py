import json
import os
from typing import List, Dict

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def fallback_recipe(ingredients: List[str]) -> List[Dict[str, object]]:
    return [
        {
            "name": "Simple Mixed Ingredient Meal",
            "ingredients": ingredients,
            "time": "25 minutes",
            "difficulty": "Easy",
            "calories": "350 kcal",
            "steps": [
                "Wash and prepare all ingredients.",
                "Chop the ingredients into small pieces.",
                "Heat olive oil in a pan.",
                "Cook the ingredients until soft.",
                "Season with salt and black pepper.",
                "Serve warm."
            ]
        }
    ]


def generate_recipes(ingredients: List[str]) -> List[Dict[str, object]]:
    if not ingredients:
        return fallback_recipe(ingredients)

    prompt = f"""
You are a professional AI cooking assistant.

Available ingredients:
{", ".join(ingredients)}

Generate 4 realistic meals using ONLY these ingredients.
You may use basic cooking essentials like water, salt, black pepper, and olive oil.
Do NOT invent additional ingredients.

IMPORTANT:
- Return ONLY valid JSON
- No markdown
- No explanations
- No extra text
- Calories must be estimated realistically
- Steps must be clear and beginner-friendly

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
            temperature=0.5,
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
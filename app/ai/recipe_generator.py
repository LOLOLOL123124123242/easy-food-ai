import json
import os
import random
from typing import List, Dict

from dotenv import load_dotenv
from openai import OpenAI


class RecipeGenerator:
    def __init__(self):
        load_dotenv()
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = "gpt-4o-mini"

    def generate_nutrition(
        self,
        recipe_name: str,
        ingredients: List[str]
    ) -> Dict[str, str]:

        ingredient_text = " ".join(ingredients).lower()
        recipe_text = recipe_name.lower()

        calories = random.randint(220, 700)
        protein = random.randint(8, 35)
        carbs = random.randint(10, 70)
        fat = random.randint(5, 30)

        if "chicken" in ingredient_text or "chicken" in recipe_text:
            protein += 20
            calories += 120

        if "salmon" in ingredient_text or "salmon" in recipe_text:
            protein += 22
            fat += 12
            calories += 180

        if "egg" in ingredient_text or "omelette" in recipe_text:
            protein += 12
            fat += 8
            calories += 100

        if "lentil" in ingredient_text:
            protein += 10
            carbs += 15

        if "rice" in ingredient_text or "pasta" in ingredient_text or "potato" in ingredient_text:
            carbs += 25
            calories += 120

        if "cheese" in ingredient_text or "butter" in ingredient_text:
            fat += 12
            calories += 120

        if "olive oil" in ingredient_text:
            fat += 10
            calories += 90

        return {
            "calories": f"{calories} kcal",
            "protein": f"{protein}g",
            "carbs": f"{carbs}g",
            "fat": f"{fat}g"
        }

    def fallback_recipe(self, ingredients: List[str]) -> List[Dict[str, object]]:
        nutrition = self.generate_nutrition(
            "Simple Mixed Ingredient Meal",
            ingredients
        )

        return [
            {
                "name": "Simple Mixed Ingredient Meal",
                "ingredients": ingredients,
                "time": "25 minutes",
                "difficulty": "Easy",
                "calories": nutrition["calories"],
                "protein": nutrition["protein"],
                "carbs": nutrition["carbs"],
                "fat": nutrition["fat"],
                "category": "Quick Meal",
                "steps": [
                    "Wash and prepare all ingredients.",
                    "Chop the ingredients into small pieces.",
                    "Heat a pan with a small amount of oil.",
                    "Cook the ingredients until soft.",
                    "Season and serve warm."
                ]
            }
        ]

    def normalize_recipe(self, recipe: Dict[str, object]) -> Dict[str, object]:
        ingredients = recipe.get("ingredients", [])

        if isinstance(ingredients, str):
            ingredients = [
                item.strip()
                for item in ingredients.split(",")
            ]

        nutrition = self.generate_nutrition(
            recipe.get("name", "Recipe"),
            ingredients
        )

        return {
            "name": recipe.get("name", "Generated Recipe"),
            "ingredients": ingredients,
            "time": recipe.get("time", "25 minutes"),
            "difficulty": recipe.get("difficulty", "Easy"),

            # Force dynamic nutrition values
            "calories": nutrition["calories"],
            "protein": nutrition["protein"],
            "carbs": nutrition["carbs"],
            "fat": nutrition["fat"],

            "category": recipe.get("category", "Healthy"),
            "steps": recipe.get("steps", [])
        }

    def generate(
        self,
        ingredients: List[str],
        user_preference: str = ""
    ) -> List[Dict[str, object]]:

        if not ingredients:
            return self.fallback_recipe(ingredients)

        preference_text = (
            user_preference.strip()
            if user_preference
            else "No special preference"
        )

        prompt = f"""
You are a professional AI cooking assistant.

Available ingredients:
{", ".join(ingredients)}

User preference:
{preference_text}

Generate 4 realistic meals using ONLY the available ingredients.
You may use basic cooking essentials like water, salt, black pepper, and olive oil.

Do NOT invent additional ingredients.

Each recipe must include:
- name
- ingredients
- time
- difficulty
- category
- steps

Allowed categories:
Healthy, Vegetarian, Low Calorie, High Protein, Quick Meal

IMPORTANT:
Return ONLY valid JSON.
No markdown.
No explanation.
Do NOT include calories, protein, carbs, or fat.
The Python backend will calculate nutrition values.

JSON format:
[
  {{
    "name": "Recipe name",
    "ingredients": ["ingredient1", "ingredient2"],
    "time": "25 minutes",
    "difficulty": "Easy",
    "category": "Healthy",
    "steps": ["Step 1", "Step 2", "Step 3"]
  }}
]
"""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0.6,
                max_tokens=1400,
            )

            text_response = response.choices[0].message.content.strip()
            recipes = json.loads(text_response)

            if not isinstance(recipes, list):
                return self.fallback_recipe(ingredients)

            return [
                self.normalize_recipe(recipe)
                for recipe in recipes
            ]

        except Exception as e:
            print(f"\nAI Recipe Generation Error: {e}")
            return self.fallback_recipe(ingredients)


recipe_generator = RecipeGenerator()


def generate_recipes(
    ingredients: List[str],
    user_preference: str = ""
) -> List[Dict[str, object]]:
    return recipe_generator.generate(ingredients, user_preference)
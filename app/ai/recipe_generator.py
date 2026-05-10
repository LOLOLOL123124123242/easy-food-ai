"""
Person 1 module: AI Recipe Generation

This file receives detected ingredients and returns meal suggestions.
Later, this can be connected to OpenAI API or another AI model.
"""

from typing import List, Dict


def generate_recipes(ingredients: List[str]) -> List[Dict[str, object]]:
    """
    Generate recipe suggestions from detected ingredients.
    
    Args:
        ingredients: List of detected ingredient names.

    Returns:
        List of recipe dictionaries.
    """
    
    if not ingredients:
        return[]

    recipes = [
        {
            "name": "Simple Ingredient Omelette",
            "ingredients": ingredients,
            "time": "15 minutes",
            "difficulty": "Easy",
            "calories": "300 kcal",
            "steps": [
                "Wash and prepare all ingredients.",
                "Cut the vegetables into small pieces.",
                "Heat a pan with a little oil.",
                "Cook the ingredients for a few minutes.",
                "Serve warm."
            ]
        },
        {
            "name": "Quick Mixed Meal",
            "ingredients": ingredients,
            "time": "20 minutes",
            "difficulty": "Easy",
            "calories": "400 kcal",
            "steps": [
                "Prepare the detected ingredients.",
                "Mix them together in a pan or bowl.",
                "Cook until everything is soft and ready.",
                "Add salt or spices if needed.",
                "Serve as a simple homemade meal."
            ]
        }
    ]

    return recipes




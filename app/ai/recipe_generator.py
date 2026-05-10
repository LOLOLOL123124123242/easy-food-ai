"""
Person 2 module: AI Recipe Generation

Replace or improve this rule-based starter with OpenAI API or another AI model.
"""

from typing import List, Dict


def generate_recipes(ingredients: List[str]) -> List[Dict[str, object]]:
    """
    Generate meal ideas from detected ingredients.

    Args:
        ingredients: List of ingredient names.

    Returns:
        List of recipe dictionaries.
    """

    ingredient_text = ", ".join(ingredients)

    # TODO: Replace this demo output with AI-generated recipes.
    recipes = [
        {
            "name": "Cheese Tomato Omelette",
            "time": "15 minutes",
            "difficulty": "Easy",
            "calories": "Approx. 320 kcal",
            "ingredients": ingredient_text,
            "steps": [
                "Chop the tomato and onion.",
                "Beat the eggs in a bowl.",
                "Cook onion and tomato in a pan for 3 minutes.",
                "Add eggs and cheese.",
                "Cook until ready and serve warm."
            ]
        },
        {
            "name": "Simple Egg and Cheese Sandwich",
            "time": "10 minutes",
            "difficulty": "Easy",
            "calories": "Approx. 280 kcal",
            "ingredients": ingredient_text,
            "steps": [
                "Cook the egg in a pan.",
                "Add cheese on top while hot.",
                "Add tomato and onion if desired.",
                "Serve with bread or salad."
            ]
        },
        {
            "name": "Tomato Egg Skillet",
            "time": "20 minutes",
            "difficulty": "Medium",
            "calories": "Approx. 350 kcal",
            "ingredients": ingredient_text,
            "steps": [
                "Slice tomato and onion.",
                "Cook them in a pan until soft.",
                "Crack eggs over the vegetables.",
                "Add cheese and cover the pan.",
                "Cook until eggs are finished."
            ]
        }
    ]

    return recipes

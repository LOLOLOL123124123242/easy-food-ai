from app.vision.ingredient_detector import detect_ingredients
from app.ai.recipe_generator import generate_recipes


def test_detect_ingredients_returns_list():
    result = detect_ingredients("demo.jpg")
    assert isinstance(result, list)


def test_generate_recipes_returns_list():
    result = generate_recipes(["tomato", "egg"])
    assert isinstance(result, list)
    assert len(result) > 0

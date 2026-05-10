from app.vision.ingredient_detector import detect_ingredients
from app.ai.recipe_generator import generate_recipes


def test_complete_ai_flow():
    """
    Test full AI pipeline
    Image -> ingredients
    """

    # Fake image path for testing
    image_path = "sample_food_image.jpg"

    # Step 1: Detect ingredients
    ingredients = detect_ingredients(image_path)

    print("Detected Ingredients")
    print(ingredients)

    # Step 2: Generate recipes
    recipes = generate_recipes(ingredients)

    print("\nGenerated Recipes:")

    for recipe in recipes:
        print(f"- {recipe['name']}")


if __name__ == "__main__":
    test_complete_ai_flow()
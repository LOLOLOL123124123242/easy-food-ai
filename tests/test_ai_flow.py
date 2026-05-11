from app.vision.ingredient_detector import detect_ingredients
from app.ai.recipe_generator import generate_recipes


def test_complete_ai_flow():
    """
    Test full AI pipeline:
    image -> ingredients -> recipes
    """

    image_path = "app/uploads/food.jpg.jpg"

    ingredients = detect_ingredients(image_path)

    print("\nDetected Ingredients:")
    print(", ".join(ingredients))

    recipes = generate_recipes(ingredients)

    print("\nGenerated Recipes:")

    for recipe in recipes:
        print("\n-------------------------")
        print(f"Meal: {recipe['name']}")
        print(f"Time: {recipe['time']}")
        print(f"Difficulty: {recipe['difficulty']}")
        print(f"Calories: {recipe['calories']}")
        print("Ingredients:", ", ".join(recipe["ingredients"]))

        print("Steps:")
        for step in recipe["steps"]:
            print(f"  - {step}")


if __name__ == "__main__":
    test_complete_ai_flow()
from app.vision.ingredient_detector import detect_ingredients
from app.ai.recipe_generator import generate_recipes


def test_complete_ai_flow():
    """
    Test full AI pipeline:
    image -> ingredients -> recipes
    """

    image_path = "app/uploads/food.jpg.jpg"

    user_preference = "healthy low calorie"

    ingredients = detect_ingredients(image_path)

    print("\nDetected Ingredients:")
    print(", ".join(ingredients))

    recipes = generate_recipes(
        ingredients,
        user_preference=user_preference
    )

    print("\nUser Preference:")
    print(user_preference)

    print("\nGenerated Recipes:")

    for recipe in recipes:
        print("\n-------------------------")
        print(f"Meal: {recipe['name']}")
        print(f"Time: {recipe['time']}")
        print(f"Difficulty: {recipe['difficulty']}")
        print(f"Calories: {recipe['calories']}")
        print(f"Protein: {recipe.get('protein', 'N/A')}")
        print(f"Carbs: {recipe.get('carbs', 'N/A')}")
        print(f"Fat: {recipe.get('fat', 'N/A')}")
        print(f"Category: {recipe.get('category', 'General')}")
        print("Ingredients:", ", ".join(recipe["ingredients"]))

        print("Steps:")
        for step in recipe["steps"]:
            print(f"  - {step}")


if __name__ == "__main__":
    test_complete_ai_flow()
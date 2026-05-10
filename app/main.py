from flask import Flask, render_template, request
from pathlib import Path

from vision.ingredient_detector import detect_ingredients
from ai.recipe_generator import generate_recipes
from database.db import init_db, save_recipe

BASE_DIR = Path(__file__).resolve().parent
UPLOAD_FOLDER = BASE_DIR / "uploads"

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = str(UPLOAD_FOLDER)

init_db()


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    image = request.files.get("ingredient_image")

    if not image or image.filename == "":
        return render_template(
            "results.html",
            error="Please upload an ingredient image.",
            ingredients=[],
            recipes=[]
        )

    image_path = UPLOAD_FOLDER / image.filename
    image.save(image_path)

    ingredients = detect_ingredients(str(image_path))
    recipes = generate_recipes(ingredients)

    return render_template(
        "results.html",
        ingredients=ingredients,
        recipes=recipes,
        error=None
    )


@app.route("/save", methods=["POST"])
def save():
    recipe_name = request.form.get("recipe_name", "Unknown Recipe")
    ingredients = request.form.get("ingredients", "")
    steps = request.form.get("steps", "")

    save_recipe(recipe_name, ingredients, steps)

    return render_template(
        "saved.html",
        recipe_name=recipe_name
    )


if __name__ == "__main__":
    app.run(debug=True)

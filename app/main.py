from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import send_from_directory

from werkzeug.utils import secure_filename

import os
import sqlite3
import random
from datetime import datetime

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/favorites")
def favorites():
    return render_template("favorites.html")


@app.route("/history")
def history():
    return render_template("history.html")


@app.route("/saved")
def saved():
    connection = sqlite3.connect("recipes.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS saved_recipes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            recipe_name TEXT,
            ingredients TEXT,
            steps TEXT,
            created_at TEXT
        )
    """)

    cursor.execute("""
        SELECT *
        FROM saved_recipes
        ORDER BY id DESC
    """)

    recipes = cursor.fetchall()

    connection.close()

    return render_template(
        "saved.html",
        recipes=recipes
    )


@app.route("/save_recipe", methods=["POST"])
def save_recipe():
    recipe_name = request.form.get("recipe_name")
    ingredients = request.form.get("ingredients")
    steps = request.form.get("steps")

    connection = sqlite3.connect("recipes.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS saved_recipes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            recipe_name TEXT,
            ingredients TEXT,
            steps TEXT,
            created_at TEXT
        )
    """)

    created_at = datetime.now().strftime("%d.%m.%Y %H:%M")

    cursor.execute("""
        INSERT INTO saved_recipes (
            recipe_name,
            ingredients,
            steps,
            created_at
        )
        VALUES (?, ?, ?, ?)
    """, (
        recipe_name,
        ingredients,
        steps,
        created_at
    ))

    connection.commit()
    connection.close()

    return redirect(url_for("saved"))


@app.route("/generate", methods=["POST"])
def generate():
    uploaded_file = request.files.get("ingredient_image")
    user_preference = request.form.get("user_preference", "").strip()

    image_filename = None

    if uploaded_file and uploaded_file.filename != "":
        filename = secure_filename(uploaded_file.filename)

        save_path = os.path.join(
            app.config["UPLOAD_FOLDER"],
            filename
        )

        uploaded_file.save(save_path)

        image_filename = filename

    if not image_filename and not user_preference:
        return render_template(
            "results.html",
            error="Please upload an image or write what you would like to eat.",
            ingredients=[],
            recipes=[],
            image_filename=None
        )

    if user_preference:
        detected_ingredients = [
            user_preference
        ]
    else:
        detected_ingredients = [
            "Tomato",
            "Cheese",
            "Chicken",
            "Onion",
            "Garlic"
        ]

    recipes = [
        {
            "name": "Chicken Pasta",
            "ingredients": "Chicken, Pasta, Tomato Sauce, Garlic",
            "steps": [
                "Boil the pasta.",
                "Cook the chicken.",
                "Add sauce and garlic.",
                "Mix everything together."
            ],
            "time": "20 min",
            "difficulty": "Easy",
            "calories": "520 kcal"
        },
        {
            "name": "Cheese Omelette",
            "ingredients": "Eggs, Cheese, Butter",
            "steps": [
                "Whisk the eggs.",
                "Cook in butter.",
                "Add cheese.",
                "Fold and serve."
            ],
            "time": "10 min",
            "difficulty": "Easy",
            "calories": "350 kcal"
        },
        {
            "name": "Garlic Chicken Rice",
            "ingredients": "Chicken, Rice, Garlic, Onion",
            "steps": [
                "Cook the rice.",
                "Fry chicken and onion.",
                "Add garlic.",
                "Serve together."
            ],
            "time": "30 min",
            "difficulty": "Medium",
            "calories": "610 kcal"
        }
    ]

    if user_preference:
        recipes.insert(
            0,
            {
                "name": f"{user_preference.title()} Recipe",
                "ingredients": user_preference,
                "steps": [
                    f"Prepare {user_preference}.",
                    "Add simple ingredients.",
                    "Cook until ready.",
                    "Serve warm."
                ],
                "time": "15 min",
                "difficulty": "Easy",
                "calories": "400 kcal"
            }
        )

    random.shuffle(recipes)

    return render_template(
        "results.html",
        ingredients=detected_ingredients,
        recipes=recipes,
        image_filename=image_filename,
        error=None
    )


@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(
        app.config["UPLOAD_FOLDER"],
        filename
    )


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import send_from_directory

from werkzeug.utils import secure_filename

from vision.ingredient_detector import detect_ingredients
from ai.recipe_generator import generate_recipes

import os
import sqlite3
from datetime import datetime

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def start():
    return render_template("login.html")


@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


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
    detected_ingredients = []

    if uploaded_file and uploaded_file.filename != "":
        filename = secure_filename(uploaded_file.filename)

        save_path = os.path.join(
            app.config["UPLOAD_FOLDER"],
            filename
        )

        uploaded_file.save(save_path)
        image_filename = filename

        detected_ingredients = detect_ingredients(save_path)

    if not detected_ingredients and user_preference:
        detected_ingredients = [user_preference]

    if not detected_ingredients and not user_preference:
        return render_template(
            "results.html",
            error="Please upload an image or write what you would like to eat.",
            ingredients=[],
            recipes=[],
            image_filename=None
        )

    recipes = generate_recipes(
        detected_ingredients,
        user_preference=user_preference
    )

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
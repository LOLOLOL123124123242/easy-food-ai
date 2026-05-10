"""
Person 3 module: SQLite Database
"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "recipes.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS saved_recipes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            recipe_name TEXT NOT NULL,
            ingredients TEXT,
            steps TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    conn.commit()
    conn.close()


def save_recipe(recipe_name: str, ingredients: str, steps: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO saved_recipes (recipe_name, ingredients, steps)
        VALUES (?, ?, ?)
        """,
        (recipe_name, ingredients, steps)
    )

    conn.commit()
    conn.close()

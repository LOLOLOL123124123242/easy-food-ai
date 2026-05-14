# Easy Food - AI Recipe App

Easy Food is a fully Python-based AI recipe application. The user uploads a picture of available ingredients, the system detects ingredients using computer vision, and then generates several meal ideas with cooking instructions.

## Main Workflow

1. User uploads an ingredient image.
2. Python vision module detects ingredients.
3. AI recipe module generates meal variations.
4. Flask displays recipes to the user.
5. Optional: user saves favorite recipes to SQLite.

## Team Work Split

### Person 1 - Computer Vision / Ingredient Detection
Folder: `app/vision/`

Responsible for:
- Image processing
- Ingredient detection
- OpenCV / YOLO integration
- Returning detected ingredients as a Python list

Main file:
- `app/vision/ingredient_detector.py`

### Person 2 - AI Recipe Generation / Backend Logic
Folder: `app/ai/`

Responsible for:
- Recipe generation from detected ingredients
- Meal variations
- Cooking steps
- Difficulty, time, calories estimation

Main file:
- `app/ai/recipe_generator.py`

### Person 3 - Flask App / UI / Database
Folders: `app/`, `app/templates/`, `app/static/`, `app/database/`

Responsible for:
- Flask routes
- Upload page
- Results page
- SQLite database
- Save favorites feature

Main files:
- `app/main.py`
- `app/database/db.py`
- `app/templates/index.html`
- `app/templates/results.html`

## Installation

```bash
pip install -r requirements.txt
```

## Run Project

```bash
python app/main.py
```

Open in browser:

```text
http://127.0.0.1:5000
```

## Notes

This ZIP contains a clean starter structure. Each team member can add their own code inside the assigned folders.

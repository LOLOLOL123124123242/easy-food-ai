# Team Task Division

## Person 1: Computer Vision

Folder: `app/vision/`

Tasks:
- Add real ingredient detection.
- Use OpenCV, YOLO, TensorFlow, or PyTorch.
- Return ingredient names as a list.

Required output format:

```python
["tomato", "egg", "cheese"]
```

## Person 2: AI Recipe Generation

Folder: `app/ai/`

Tasks:
- Generate various meals from ingredients.
- Add cooking time, difficulty, calories, and steps.
- Later, connect OpenAI API or another AI model.

Required output format:

```python
[
    {
        "name": "Recipe Name",
        "time": "15 minutes",
        "difficulty": "Easy",
        "calories": "300 kcal",
        "ingredients": "tomato, egg",
        "steps": ["Step 1", "Step 2"]
    }
]
```

## Person 3: Flask UI and Database

Folders: `app/`, `app/templates/`, `app/static/`, `app/database/`

Tasks:
- Improve web pages.
- Improve upload page.
- Display detected ingredients and recipes.
- Add save recipe and favorite recipe features.

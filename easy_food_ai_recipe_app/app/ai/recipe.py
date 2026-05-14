class Recipe:
    def __init__(
        self,
        name,
        ingredients,
        time,
        difficulty,
        calories,
        protein,
        carbs,
        fat,
        category,
        steps
    ):
        self.name = name
        self.ingredients = ingredients
        self.time = time
        self.difficulty = difficulty
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat
        self.category = category
        self.steps = steps

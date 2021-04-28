class Dish:

    def __init__(self, name: str, ingredients: list):
        self.name = name
        self.ingredients = ingredients

    def __str__(self):
        s = f'- {self.name}:\n'
        for ingredient in self.ingredients:
            s += f'\t{ingredient}\n'
        return s

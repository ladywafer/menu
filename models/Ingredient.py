class Ingredient:

    def __init__(self, name: str, unit: str):
        self.name = name
        self.unit = unit

    def __str__(self):
        return f'{self.name} {self.unit}'

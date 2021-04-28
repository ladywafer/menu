class Menu:

    def __init__(self, dishes: list):
        self.dishes = dishes

    def __str__(self):
        s = ""
        for dish in self.dishes:
            s += f'{dish}'
        return s

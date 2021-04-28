import json

from models.DIsh import Dish
from models.Ingredient import Ingredient
from models.Menu import Menu


def load(path: str, menu: Menu = Menu([])):
    with open(path, 'r') as json_file:
        data = json.load(json_file)
        for dish in data["dishes"]:
            d = Dish(dish["name"], [])
            for ingredient in dish["ingredients"]:
                i = Ingredient(ingredient["name"], ingredient["unit"])
                d.ingredients.append(i)
            menu.dishes.append(d)
    return menu

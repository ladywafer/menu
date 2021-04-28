from src.models.Menu import Menu


def find_by_dish(menu: Menu, pattern: str):
    new_menu = Menu([])
    for dish in menu.dishes:
        if pattern.lower() in dish.name.lower():
            new_menu.dishes.append(dish)
    return new_menu


def find_by_ingredient(menu: Menu, pattern: str):
    new_menu = Menu([])
    for dish in menu.dishes:
        for ingredient in dish.ingredients:
            if pattern.lower() in ingredient.name.lower():
                new_menu.dishes.append(dish)
                break
    return new_menu

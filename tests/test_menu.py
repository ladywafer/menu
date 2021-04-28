from unittest import TestCase

from src.db.loader import load
from src.finds.finds import find_by_dish, find_by_ingredient
from src.models.DIsh import Dish
from src.models.Ingredient import Ingredient
from src.models.Menu import Menu


class TestMenu(TestCase):

    def test_ingredient_str(self):
        arr = [
            {"name": "name 1", "unit": "unit 1", "str": "name 1 unit 1"},
            {"name": "name 2", "unit": "unit 2", "str": "name 2 unit 2"},
            {"name": "name 3", "unit": "unit 3", "str": "name 3 unit 3"},
        ]
        for i in arr:
            ingredient = Ingredient(i["name"], i["unit"])
            self.assertEqual(i["str"], str(ingredient))

    def test_dish_str(self):
        arr = [
            {"name": "name 1", "ingredients": [], "str": "- name 1:\n"},
            {"name": "name 2", "ingredients": [Ingredient("name", "unit")], "str": "- name 2:\n\tname unit\n"},
            {"name": "name 2", "ingredients": [
                Ingredient("name 1", "unit 1"),
                Ingredient("name 2", "unit 2"),
            ], "str": "- name 2:\n\tname 1 unit 1\n\tname 2 unit 2\n"},
        ]
        for i in arr:
            dish = Dish(i["name"], i["ingredients"])
            self.assertEqual(i["str"], str(dish))

    def test_menu_str(self):
        arr = [
            {"dishes": [], "str": ""},
            {"dishes": [Dish("name", [])], "str": "- name:\n"},
        ]
        for i in arr:
            menu = Menu(i["dishes"])
            self.assertEqual(i["str"], str(menu))

    def test_load_file(self):
        menu = load("menu.json", Menu([]))
        self.assertEqual(2, len(menu.dishes))

    def test_find_by_dish_name(self):
        menu = find_by_dish(load("menu.json", Menu([])), "яич")
        self.assertEqual(1, len(menu.dishes))

    def test_find_by_ingredient(self):
        menu = find_by_ingredient(load("menu.json", Menu([])), "сол")
        self.assertEqual(1, len(menu.dishes))

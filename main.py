from src.db.loader import load
from src.finds.finds import find_by_dish, find_by_ingredient
from src.models.Menu import Menu

menu = load("menu.json", Menu([]))

while True:
    print(
        """Меню приложения:
        1 - вывести всё меню
        2 - поиск блюд по названию
        3 - поиск блюд по названию ингрудиента
        4 - загрузка меню
        5 - очистить меню
        6 - выход"""
    )
    n = int(input("Введите номер пункта меню: "))
    if n == 1:
        print(menu)
    if n == 2:
        pattern = input("Введите название блюда или его часть: ")
        print(find_by_dish(menu, pattern))
    if n == 3:
        pattern = input("Введите название ингредиента или его часть: ")
        print(find_by_ingredient(menu, pattern))
    if n == 4:
        path = input("Введите путь к json файлу с меню: ")
        menu = load(path, menu)
    if n == 5:
        menu = Menu([])
    if n == 6:
        break
print("Пока")

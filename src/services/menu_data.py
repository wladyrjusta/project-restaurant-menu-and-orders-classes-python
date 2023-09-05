import csv
from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes_file = self.get_dishes_from_file(source_path)
        self.dishes_list = self.create_dishes_list(self.dishes_file)
        self.dishes = set(self.create_dishes_instances(self.dishes_list))

    def get_dishes_from_file(self, source_path: str):
        with open(source_path, encoding="utf-8") as file:
            dishes = list(csv.DictReader(file, delimiter=",", quotechar='"'))
            return dishes

    def create_dishes_list(self, dishes_file):
        dishes_dict = {}
        for dish in dishes_file:
            if dish['dish'] in dishes_dict:
                dishes_dict[dish['dish']]['ingredients'].append(
                    (dish['ingredient'], dish['recipe_amount'])
                )
            else:
                dishes_dict[dish['dish']] = {}
                dishes_dict[dish['dish']]['price'] = dish['price']
                dishes_dict[dish['dish']]['ingredients'] = []
                dishes_dict[dish['dish']]['ingredients'].append(
                    (dish['ingredient'], dish['recipe_amount'])
                )
        return dishes_dict

    def create_dishes_instances(self, dishes_list):
        instances_list = []
        for dish, dish_details in dishes_list.items():
            instance = Dish(dish, float(dish_details['price']))
            for ingredient, amount in dish_details['ingredients']:
                ingredient_class = Ingredient(ingredient)
                instance.add_ingredient_dependency(
                    ingredient_class, int(amount)
                )
            instances_list.append(instance)
        return instances_list

    def __str__(self) -> str:
        return f"{self.dishes}"


menu = MenuData("tests/mocks/menu_base_data.csv")
print(menu)

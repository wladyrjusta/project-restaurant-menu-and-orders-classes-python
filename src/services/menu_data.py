import csv
from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.__source_path = source_path
        self.__dishes_file = self.__get_dishes_from_file(self.__source_path)
        self.__dishes_list = self.__create_dishes_list(self.__dishes_file)
        self.dishes = set(self.__create_dishes_instances(self.__dishes_list))

    def __get_dishes_from_file(self, source_path: str):
        with open(source_path, encoding="utf-8") as file:
            dishes = list(csv.DictReader(file, delimiter=",", quotechar='"'))
            return dishes

    def __create_dishes_list(self, dishes_file):
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

    def __create_dishes_instances(self, dishes_list):
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

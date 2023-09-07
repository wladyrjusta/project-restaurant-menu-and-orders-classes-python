from typing import Dict, List

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str) -> None:
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    def __str__(self) -> str:
        return f"{self}"

    # Req 4
    def get_main_menu(self, restriction=None) -> List[Dict]:
        menu_list = []
        for dish in self.menu_data.dishes:
            has_restriction = self.__verify_restrictions(dish, restriction)
            if has_restriction is False:
                has_ingredients = self.__has_ingredients_in_inventory(dish)
                if has_ingredients is False:
                    return []
                else:
                    self.__dish_dict_generate(dish, menu_list)
        return menu_list

    def __verify_restrictions(self, dish, restriction=None):
        restrictions_set = {
            restrictions for restrictions in dish.get_restrictions()
        }
        return restriction in restrictions_set

    def __has_ingredients_in_inventory(self, dish):
        inventory_set = self.inventory.inventory
        ingredients_list = {
            ingredient for ingredient in dish.get_ingredients()
        }
        has_ingredients = ingredients_list.issubset(inventory_set)
        return has_ingredients

    def __dish_dict_generate(self, dish, menu_list):
        menu_list.append({
            'dish_name': dish.name,
            'ingredients': [
                ingredient for ingredient in dish.get_ingredients()
                ],
            'price': dish.price,
            'restrictions': [
                restrictions for restrictions in dish
                .get_restrictions()
                ],
            })

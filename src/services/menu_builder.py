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
        if len(self.inventory.inventory) < 3:
            return []
        menu_list = []
        for dish in self.menu_data.dishes:
            restrictions_list = [
                ingredient.restrictions for ingredient in dish.recipe
            ]
            has_restriction = any(
                restriction in conjunto for conjunto in restrictions_list
            )
            if has_restriction is False:
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
        return menu_list


menu = MenuBuilder(
    data_path="tests/mocks/menu_base_data.csv",
    inventory_path="tests/mocks/inventory_base_data.csv",
)
menu.get_main_menu()
# print([ingredient for dish in menu.menu_data.dishes
#       for ingredient in dish.get_ingredients()])

# for dish in menu.menu_data.dishes:
#     ingredients_list = [ingredient for ingredient in dish.get_ingredients()]
# inventory_list = menu.inventory.inventory
# print(
#       ingredients_list,
#       inventory_list,
#       inventory_list in ingredients_list)

# for dish in menu.menu_data.dishes:
#     for restrictions in dish.get_restrictions():
#         print(restrictions)
# print([
#     value.value for restrictions_set in restrictions_list
#     for value in restrictions_set
# ])

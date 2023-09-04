from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient_1 = Ingredient("queijo parmesão")
    ingredient_2 = Ingredient("queijo parmesão")
    assert ingredient_1.__hash__() == ingredient_2.__hash__()
    assert ingredient_1.__eq__(ingredient_2) is not False
    assert ingredient_1.__repr__() == "Ingredient('queijo parmesão')"

    different_ingredient_1 = Ingredient("queijo parmesão")
    different_ingredient_2 = Ingredient("presunto")
    assert (
        different_ingredient_1.__hash__() != different_ingredient_2.__hash__()
    )
    assert different_ingredient_1.__eq__(different_ingredient_2) is not True
    assert different_ingredient_1.name == "queijo parmesão"
    assert (
        different_ingredient_1.restrictions == {
            Restriction.LACTOSE, Restriction.ANIMAL_DERIVED
        }
    )

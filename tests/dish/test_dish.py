import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction


# Req 2
def test_dish():
    spaghetti_1 = Dish('spaghetti', 20.99)
    spaghetti_2 = Dish('spaghetti', 20.99)
    sandwich = Dish('Sandwich', 1.99)
    ham = Ingredient('presunto')
    assert spaghetti_1.name == 'spaghetti'
    assert spaghetti_1.__hash__() == spaghetti_2.__hash__()
    assert spaghetti_1.__hash__() is not sandwich.__hash__()
    assert (spaghetti_1 == spaghetti_2) is True
    assert sandwich.__repr__() == "Dish('Sandwich', R$1.99)"
    with pytest.raises(TypeError, match="Dish price must be float."):
        sandwich = Dish('Sandwich', '1')
    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        sandwich = Dish('Sandwich', -1)
    sandwich.add_ingredient_dependency(ham, 25)
    assert sandwich.recipe.get(ham) == 25
    assert sandwich.get_restrictions() == {
            Restriction.ANIMAL_MEAT,
            Restriction.ANIMAL_DERIVED,
        }
    assert sandwich.get_ingredients() == {ham}

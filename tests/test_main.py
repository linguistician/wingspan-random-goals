import main
from src.wingspan.tile import Tile


def test_get_random_tile_with_zero_items():
    try:
        assert main.get_random_tile(())
    except ValueError:
        assert True


def test_get_random_tile_with_one_item():
    ex = Tile("Beak Pointing Left", "Beak Pointing Right", "Oceania")
    assert main.get_random_tile([ex]) == ex


def test_get_random_goals_with_number_of_items_less_than_number_of_goals():
    pile = (
        Tile("Cubes on 'Play a Bird'", "Birds Worth ≤3 VP", "Oceania"),
        Tile("Brown Powers", "White & No Powers", "European"),
    )
    try:
        assert main.get_random_goals(pile)
    except ValueError:
        assert True

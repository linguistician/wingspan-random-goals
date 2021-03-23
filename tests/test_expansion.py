from src.wingspan.expansions import Original, European, Oceania, WingspanInterface
from src.wingspan.tile import Tile


def test_interface():
    assert issubclass(Oceania, WingspanInterface)
    assert issubclass(European, WingspanInterface)
    assert issubclass(Original, WingspanInterface)


def test_expansion_tiles():
    oe = Oceania()
    assert (
               Tile("Cubes on 'Play a Bird'", "Birds Worth ≤3 VP", "Oceania"),
               Tile("Invertebrate in Food Cost of Your Birds", "Fruit + Wheat in Food Cost of Your Birds", "Oceania"),
               Tile("Beak Pointing Left", "Beak Pointing Right", "Oceania"),
               Tile("No Goal", "Rat + Fish in Food Cost of Your Birds", "Oceania"),
           ) == oe.get_tiles()
    ee = European()
    assert (
        Tile("Food in Personal Supply", "Cards in Hand", "European"),
        Tile("Birds with Tucked Cards", "Food Cost of Played Birds", "European"),
        Tile("Birds Worth >4 VP", "Birds With No Eggs", "European"),
        Tile("Brown Powers", "White & No Powers", "European"),
        Tile("Birds in One Row", "Filled Columns", "European"),
    ) == ee.get_tiles()
    og = Original()
    assert (
        Tile("Total Birds", "Sets of 3 Eggs in All Habitats", "Original"),
        Tile("Birds in Grassland", "Eggs in Grassland", "Original"),
        Tile("Cavity Birds With Eggs", "Eggs in Cavity", "Original"),
        Tile("Bowl Birds With Eggs", "Eggs in Bowl", "Original"),
        Tile("Birds in Wetland", "Eggs in Wetland", "Original"),
        Tile("Platform Birds With Eggs", "Eggs in Platform", "Original"),
        Tile("Birds in Forest", "Eggs in Forest", "Original"),
        Tile("Ground Birds With Eggs", "Eggs in Ground", "Original"),
    ) == og.get_tiles()

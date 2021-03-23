import abc
from typing import Tuple
from src.wingspan.tile import Tile


class WingspanInterface(metaclass=abc.ABCMeta):
    """
    A formal interface for the version(s) of Wingspan.
    """
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'get_tiles') and
                callable(subclass.get_tiles))


class Oceania:
    """
    Oceania Expansion in Wingspan.

    __tiles: The tiles from Oceania Expansion.
    """
    __tiles: Tuple[Tile, ...]

    def __init__(self):
        self.__tiles = (
            Tile("Cubes on 'Play a Bird'", "Birds Worth ≤3 VP", self.__class__.__name__),
            Tile("Invertebrate in Food Cost of Your Birds", "Fruit + Wheat in Food Cost of Your Birds",
                 self.__class__.__name__),
            Tile("Beak Pointing Left", "Beak Pointing Right", self.__class__.__name__),
            Tile("No Goal", "Rat + Fish in Food Cost of Your Birds", self.__class__.__name__),
        )

    def get_tiles(self) -> Tuple[Tile]:
        return self.__tiles


class European:
    """
    European Expansion in Wingspan.

    __tiles: The tiles from European Expansion.
    """
    __tiles: Tuple[Tile, ...]

    def __init__(self):
        self.__tiles = (
            Tile("Food in Personal Supply", "Cards in Hand", self.__class__.__name__),
            Tile("Birds with Tucked Cards", "Food Cost of Played Birds", self.__class__.__name__),
            Tile("Birds Worth >4 VP", "Birds With No Eggs", self.__class__.__name__),
            Tile("Brown Powers", "White & No Powers", self.__class__.__name__),
            Tile("Birds in One Row", "Filled Columns", self.__class__.__name__),
        )

    def get_tiles(self) -> Tuple[Tile]:
        return self.__tiles


class Original:
    """
    Base game of Wingspan.

    __tiles: The tiles from the base game.
    """
    __tiles: Tuple[Tile, ...]

    def __init__(self):
        self.__tiles = (
            Tile("Total Birds", "Sets of 3 Eggs in All Habitats", self.__class__.__name__),
            Tile("Birds in Grassland", "Eggs in Grassland", self.__class__.__name__),
            Tile("Cavity Birds With Eggs", "Eggs in Cavity", self.__class__.__name__),
            Tile("Bowl Birds With Eggs", "Eggs in Bowl", self.__class__.__name__),
            Tile("Birds in Wetland", "Eggs in Wetland", self.__class__.__name__),
            Tile("Platform Birds With Eggs", "Eggs in Platform", self.__class__.__name__),
            Tile("Birds in Forest", "Eggs in Forest", self.__class__.__name__),
            Tile("Ground Birds With Eggs", "Eggs in Ground", self.__class__.__name__),
        )

    def get_tiles(self) -> Tuple[Tile]:
        return self.__tiles

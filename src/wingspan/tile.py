from dataclasses import dataclass


@dataclass(frozen=True)
class Tile:
    """
    A tile in Wingspan.

    front: The front goal.

    back: The back goal.

    game_version: The version of the game that has the tile.
    """
    front: str
    back: str
    game_version: str

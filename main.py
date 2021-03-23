import random
from typing import List, Tuple, Sequence
from src.wingspan.expansions import Oceania, European, Original
from src.wingspan.tile import Tile


def get_random_tile(tiles: Sequence[Tile]) -> Tile:
    """
    Returns a random tile.

    Args:
        tiles: A group of tiles.

    Returns:
        A random tile.

    Raises:
        ValueError: If `tiles` has zero items.
    """
    if not tiles:
        raise ValueError("tiles cannot have zero items.")
    total: int = len(tiles)
    rand: int = random.randrange(total)
    return tiles[rand]


def get_goal(tile: Tile) -> str:
    """
    Returns an end-of-round goal from the tile.

    Args:
        tile: A Wingspan tile.

    Returns:
        An end-of-round goal.
    """
    SIDES: int = 2
    revealed: int = random.randrange(SIDES)
    if revealed:
        return f"{tile.back} ({tile.game_version})"
    return f"{tile.front} ({tile.game_version})"


def get_random_goals(tiles: Sequence[Tile]) -> List[str]:
    """
    Returns 4 random end-of-round goals for Wingspan.

    Args:
        tiles: A group of tiles.

    Returns:
        4 random end-of-round goals.

    Raises:
        ValueError: If the length of `tiles` is less than NUM_OF_GOALS.
    """
    NUM_OF_GOALS: int = 4
    if len(tiles) < NUM_OF_GOALS:
        raise ValueError("The length of tiles cannot be less than NUM_OF_GOALS.")
    duplicate_tiles: List[Tile] = list(tiles)
    round_goals: List[str] = []
    for tile in range(NUM_OF_GOALS):
        selected: Tile = get_random_tile(duplicate_tiles)
        goal: str = get_goal(selected)
        round_goals.append(goal)
        duplicate_tiles.remove(selected)
    return round_goals


def print_goals(goals: List[str]):
    """
    Prints the end-of-round goals.

    Args:
        goals: The end-of-round goals in Wingspan.
    """
    text: str = "\n"
    for num, goal in enumerate(goals):
        text += f"\tR{num+1}: {goal}\n"
    print(text)


if __name__ == "__main__":
    oe: Tuple[Tile] = Oceania().get_tiles()
    ee: Tuple[Tile] = European().get_tiles()
    og: Tuple[Tile] = Original().get_tiles()
    bag: Tuple[Tile, ...] = oe + ee + og
    end_of_rounds: List[str] = get_random_goals(bag)
    print_goals(end_of_rounds)


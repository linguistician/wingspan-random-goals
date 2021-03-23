from src.wingspan.tile import Tile


def test_construction():
    t = Tile('Beak Pointing Left', 'Beak Pointing Right')
    assert 'Beak Pointing Left' == t.front
    assert 'Beak Pointing Right' == t.back



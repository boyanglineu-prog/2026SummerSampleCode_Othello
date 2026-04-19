from tiles import Tiles
from game_controller import GameController


def make_tiles(line_cap=8, spacing=100):
    """Helper: create a standard 8x8 board with a GameController."""
    width = line_cap * spacing
    height = line_cap * spacing
    gc = GameController(width, height, spacing)
    tiles = Tiles(width, height, spacing, gc)
    return tiles, gc


def test_initialize():
    tiles, gc = make_tiles()

    assert len(tiles.tiles) == tiles.LINE_CAP

    center = tiles.LINE_CAP // 2  # 4
    x1 = center - 1  # 3
    x2 = center  # 4
    y1 = center - 1  # 3
    y2 = center  # 4

    # (3,3) white, (3,4) black, (4,3) black, (4,4) white
    assert tiles.tiles[x1][y1] is not None
    assert tiles.tiles[x1][y1].color == "white"

    assert tiles.tiles[x1][y2] is not None
    assert tiles.tiles[x1][y2].color == "black"

    assert tiles.tiles[x2][y1] is not None
    assert tiles.tiles[x2][y1].color == "black"

    assert tiles.tiles[x2][y2] is not None
    assert tiles.tiles[x2][y2].color == "white"

    # Tile/GC colors synced
    assert tiles.tile_color == "black"
    assert tiles.tile_oppo_color == "white"
    assert gc.turn == "black"


def test_cal_index():
    tiles, gc = make_tiles(spacing=100)

    row, col = tiles.cal_index(tile_x=150, tile_y=250)
    assert row == 2
    assert col == 1


def test_update_leagle_moves():
    tiles, gc = make_tiles()

    # for the first move
    expected_keys = {(2, 3), (3, 2), (4, 5), (5, 4)}
    actual_keys = set(tiles.leagle_moves.keys())

    assert actual_keys == expected_keys

    tiles.tile_row, tiles.tile_col = (2, 3)
    assert tiles.is_leagle_move() is True

    tiles.tile_row, tiles.tile_col = (5, 4)
    assert tiles.is_leagle_move() is True

    tiles.tile_row, tiles.tile_col = (0, 0)
    assert tiles.is_leagle_move() is False

    tiles.tile_row, tiles.tile_col = (666, 666)
    assert tiles.is_leagle_move() is False


def test_ai_pick():
    tiles, gc = make_tiles()

    row, col = tiles.ai_pick()

    assert (row, col) in tiles.leagle_moves


def test_count_winner():
    tiles, gc = make_tiles()

    # Initial 4 tiles
    tiles.count_winner()

    assert gc.black_count == 2
    assert gc.white_count == 2
    assert gc.tie is True
    assert gc.black_wins is False
    assert gc.white_wins is False

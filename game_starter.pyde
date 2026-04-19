from board import Board
from game_controller import GameController
from tiles import Tiles

WIDTH = 800
HEIGHT = 800
SPACING = 100
GREEN_RGB = (0, 0.5, 0)
DELAY_TIME = 1250

ai_pending = False
ai_time = 0

game_controller = GameController(WIDTH, HEIGHT, SPACING)
board = Board(WIDTH, HEIGHT, SPACING)
tiles = Tiles(WIDTH, HEIGHT, SPACING, game_controller)


def setup():
    size(WIDTH, HEIGHT)
    colorMode(RGB, 1)


def draw():
    background(*GREEN_RGB)
    board.display()
    game_controller.display_next_tile(mouseX, mouseY)

    global ai_pending, ai_time
    # if it's ai's turn, and ai has been waiting long enough
    if ai_pending and millis() >= ai_time:
        tiles.ai_goes()
        ai_pending = False
        # senario 2, ai trigered by ai
        if tiles.tile_color == "white" and len(tiles.leagle_moves) > 0:
            # if the next round is still ai
            ai_pending = True  # set true, wait for next round draw()
            ai_time = millis() + DELAY_TIME

    tiles.display()
    game_controller.display_score_board()

    if game_controller.black_wins or game_controller.white_wins or game_controller.tie:
        if not game_controller.logged:
            game_controller.update_log(
                game_controller.black_count, game_controller.white_count
            )
            game_controller.logged = True


def mousePressed():
    """Detect mouse click, pass mouseX mouseY to black moves"""
    global ai_pending, ai_time
    if tiles.tile_color == "black":
        tiles.player_goes(mouseX, mouseY)
        # senario 1, ai trigered by player
        if tiles.tile_color == "white" and len(tiles.leagle_moves) > 0:
            ai_pending = True
            ai_time = millis() + DELAY_TIME

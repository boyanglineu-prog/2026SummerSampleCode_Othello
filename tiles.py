from tile import Tile
from game_controller import GameController
import random


class Tiles:
    """A collection of tiles."""

    def __init__(self, WIDTH, HEIGHT, SPACING, game_controller):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.SPACING = SPACING
        self.LINE_CAP = self.WIDTH // self.SPACING

        self.tiles = None  # A 2-D list of to store tiles
        self.tile_color = "black"
        self.tile_oppo_color = "white"
        self.tile_row = 0
        self.tile_col = 0
        self.leagle_moves = {}  # A dictionary to update and store leagle moves

        self.gc = game_controller
        self.gc.turn = self.tile_color

        self.ai_mode = True

        self.initialize()

    def initialize(self):
        """Generate the matrix of Nones for storing tile objects,
        place the four tiles in the center,
        fill up the leagle_moves for the first move,
        None -> None"""
        # set up place holder
        self.tiles = [
            [None for _ in range(self.LINE_CAP)] for _ in range(self.LINE_CAP)
        ]

        # put the first four tiles
        x_1 = self.LINE_CAP // 2 - 1
        x_2 = self.LINE_CAP // 2
        y_1 = self.LINE_CAP // 2 - 1
        y_2 = self.LINE_CAP // 2

        self.add_tile(x_1, y_1, "white")
        self.add_tile(x_1, y_2, "black")
        self.add_tile(x_2, y_1, "black")
        self.add_tile(x_2, y_2, "white")

        # initialize the leagle_moves list, for the first black move
        self.update_leagle_moves()

    def player_goes(self, tile_x, tile_y):
        """Player goes
        int, int -> None"""
        # calculate row and col
        self.tile_row, self.tile_col = self.cal_index(tile_x, tile_y)

        # if it is not a leagle move, return and wait for next click
        if not self.is_leagle_move():
            return

        # if leagle, add a tile
        self.add_tile(self.tile_row, self.tile_col, self.tile_color)

        # update colors, before switch turn
        self.update_color()

        # switch turn
        self.switch_turn()

        # update leagle_moves
        self.update_leagle_moves()

        # now on white
        if len(self.leagle_moves) == 0:  # no leagle for white
            self.switch_turn()  # back to black
            self.update_leagle_moves()  # on black
            if len(self.leagle_moves) != 0:  # black has leagle
                return  # return and wait for next click;
            else:  # black has no leagle either
                self.count_winner()  # call it an end
                return

    def ai_goes(self):
        """Computer goes
        None -> None"""
        # time.sleep(self.DELAY_TIME)
        # No, cannot sleep here, it will block draw() and freeze the screen

        # pick a position
        if self.ai_mode:
            self.tile_row, self.tile_col = self.ai_pick()
        else:
            self.tile_row, self.tile_col = random.choice(list(self.leagle_moves.keys()))

        # add a tile
        self.add_tile(self.tile_row, self.tile_col, self.tile_color)

        # update colors, before switch turn
        self.update_color()

        # switch turn
        self.switch_turn()

        # update leagle_moves
        self.update_leagle_moves()

        # now on black
        if len(self.leagle_moves) == 0:  # no leagle for black
            self.switch_turn()  # back to white
            self.update_leagle_moves()  # on white
            if len(self.leagle_moves) != 0:  # white has leagle
                return  # return in peace, game_starter will take care of the repeat
            else:  # white has no leagle either
                self.count_winner()  # call it an end
                return

    def ai_pick(self):
        """Ai algorithm, pick a better position
        scan every leagle move, return the one that flip the most tiles(winning most points)
        None -> int, int"""
        ai_row = 0
        ai_col = 0
        max_count = 0
        for start_row, start_col in self.leagle_moves.keys():
            # test every possible move
            count = 0
            for end_row, end_col in self.leagle_moves[(start_row, start_col)]:
                count += max(abs(end_row - start_row - 1), abs(end_col - start_col - 1))
            if count > max_count:
                max_count = count
                ai_row, ai_col = start_row, start_col
        return ai_row, ai_col

    def cal_index(self, tile_x, tile_y):
        """Calculate the row and col index
        int, int -> int, int"""
        row = tile_y // self.SPACING
        col = tile_x // self.SPACING
        return row, col

    def is_leagle_move(self):
        """Check if this position is leagle
        None -> boolean"""
        indices = (self.tile_row, self.tile_col)

        if indices in self.leagle_moves:
            return True
        return False

    def add_tile(self, row, col, color):
        """New a tile, convert row, col to x, y
        add to self.tiles
        int, int, str -> None"""
        standard_tile_x = (col * self.SPACING) + (self.SPACING // 2)
        standard_tile_y = (row * self.SPACING) + (self.SPACING // 2)

        new_tile = Tile(standard_tile_x, standard_tile_y, color)

        self.tiles[row][col] = new_tile

    def update_color(self):  # before switch turn
        """Flip colors of other tiles if necessary
        None -> None"""
        for end_row, end_col in self.leagle_moves[(self.tile_row, self.tile_col)]:
            row_step = (
                0
                if end_row == self.tile_row
                else (1 if end_row > self.tile_row else -1)
            )
            col_step = (
                0
                if end_col == self.tile_col
                else (1 if end_col > self.tile_col else -1)
            )

            m = self.tile_row + row_step
            n = self.tile_col + col_step

            # flip until we reach the endpoint (exclusive)
            while (m, n) != (end_row, end_col):
                self.tiles[m][n].color = self.tile_color
                m += row_step
                n += col_step

    def update_leagle_moves(self):  # after switch turn
        """Update self.leagle_moves for next round
        None -> None"""
        directions = [
            (0, 1),  # E
            (0, -1),  # W
            (1, 0),  # S
            (-1, 0),  # N
            (1, 1),  # SE
            (1, -1),  # SW
            (-1, 1),  # NE
            (-1, -1),  # NW
        ]

        self.leagle_moves.clear()  # reset first

        for row in range(self.LINE_CAP):
            for col in range(self.LINE_CAP):
                if self.tiles[row][col] is not None:
                    continue

                # set up key first, then find value from eight directions
                key = (row, col)

                for step in directions:
                    chance = False
                    m = row + step[0]
                    n = col + step[1]
                    while m >= 0 and m < self.LINE_CAP and n >= 0 and n < self.LINE_CAP:
                        if self.tiles[m][n] is None:
                            break

                        if self.tiles[m][n].color == self.tile_oppo_color:
                            chance = True
                            m += step[0]
                            n += step[1]
                            continue

                        if self.tiles[m][n].color == self.tile_color:
                            if chance:
                                # if a potential pair found
                                value = (m, n)
                                self.leagle_moves.setdefault(key, []).append(value)
                            break

    def switch_turn(self):
        """Switch turn
        inform gc accordingly
        None -> None"""
        self.tile_color, self.tile_oppo_color = self.tile_oppo_color, self.tile_color
        self.gc.turn = self.tile_color

    def count_winner(self):
        """Check who is winner,
        inform gc accordingly
        None -> None"""
        white_count = 0
        black_count = 0
        for m in range(self.LINE_CAP):
            for n in range(self.LINE_CAP):
                if self.tiles[m][n] is None:
                    continue

                if self.tiles[m][n].color == "black":
                    black_count += 1
                else:
                    white_count += 1

        self.gc.black_count = black_count
        self.gc.white_count = white_count

        if black_count > white_count:
            self.gc.black_wins = True
        elif black_count < white_count:
            self.gc.white_wins = True
        else:
            self.gc.tie = True

    def display(self):
        """Calls each tile's display method"""
        for m in range(self.LINE_CAP):
            for n in range(self.LINE_CAP):
                if self.tiles[m][n] is not None:
                    self.tiles[m][n].display()

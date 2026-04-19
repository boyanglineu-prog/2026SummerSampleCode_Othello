from tile import Tile


class GameController:
    """Maintains the state of the game."""

    def __init__(self, WIDTH, HEIGHT, SPACING):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.SPACING = SPACING
        self.TEXT_SIZE = self.WIDTH * 0.125 * 0.7
        self.TEXT_COLOR = (1, 0, 0)
        self.RECT_W = self.WIDTH * 0.875
        self.RECT_H = self.HEIGHT * 0.25
        self.RECT_X = self.WIDTH / 2 - self.RECT_W / 2
        self.RECT_Y = self.HEIGHT / 2 - self.RECT_H / 2
        self.RECT_COLOR = (1, 1, 1, 0.9)
        self.RECT_CONOR = 20

        self.black_wins = False
        self.white_wins = False
        self.tie = False
        self.black_count = 0
        self.white_count = 0
        self.logged = False
        self.turn = "black"
        self.mouse_tile = Tile(0, 0, self.turn)

    def display_next_tile(self, mouseX, mouseY):
        """Display the next tile, tracing mouse
        int, int -> None"""
        if self.turn == "black":
            self.mouse_tile.x = mouseX / self.SPACING * self.SPACING + self.SPACING / 2
            self.mouse_tile.y = mouseY / self.SPACING * self.SPACING + self.SPACING / 2
            self.mouse_tile.color = self.turn
            self.mouse_tile.display()
        # if it's computer's turn, just don't show

    def display_score_board(self):
        """Check who wins
        None -> None"""
        if self.black_wins:
            fill(*self.RECT_COLOR)
            noStroke()
            rect(self.RECT_X, self.RECT_Y, self.RECT_W, self.RECT_H, self.RECT_CONOR)

            fill(*self.TEXT_COLOR)
            textSize(self.TEXT_SIZE)
            textAlign(CENTER, CENTER)
            text(
                "PLAYER WINS\nBLACK %d : %d WHITE"
                % (self.black_count, self.white_count),
                self.WIDTH / 2,
                self.HEIGHT / 2,
            )

        elif self.white_wins:
            fill(*self.RECT_COLOR)
            noStroke()
            rect(self.RECT_X, self.RECT_Y, self.RECT_W, self.RECT_H, self.RECT_CONOR)

            fill(*self.TEXT_COLOR)
            textSize(self.TEXT_SIZE)
            textAlign(CENTER, CENTER)
            text(
                "AI WINS\nBLACK %d : %d WHITE" % (self.black_count, self.white_count),
                self.WIDTH / 2,
                self.HEIGHT / 2,
            )

        elif self.tie:
            fill(*self.RECT_COLOR)
            noStroke()
            rect(self.RECT_X, self.RECT_Y, self.RECT_W, self.RECT_H, self.RECT_CONOR)

            fill(*self.TEXT_COLOR)
            textSize(self.TEXT_SIZE)
            textAlign(CENTER, CENTER)
            text(
                "TIE",
                self.WIDTH / 2,
                self.HEIGHT / 2,
            )

    def update_log(self, black_count, white_count):
        """Uptade scores.txt
        int, int -> None"""
        with open("scores.txt", "r") as file:
            lines = file.readlines()

            total_games = int(lines[0].split(":")[1].strip())
            black_wins = int(lines[1].split(":")[1].strip())
            white_wins = int(lines[2].split(":")[1].strip())

        total_games += 1
        if black_count > white_count:
            black_wins += 1
        elif white_count > black_count:
            white_wins += 1

        with open("scores.txt", "w") as file:
            file.write("Total number of games recorded: %d\n" % total_games)
            file.write("Total number of wins by Black: %d\n" % black_wins)
            file.write("Total number of wins by White: %d\n" % white_wins)

class Board:
    """The board / grid."""

    def __init__(self, WIDTH, HEIGHT, SPACING):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.SPACING = SPACING
        self.BLACK_RGB = (0, 0, 0)

    def display(self):
        """display the board
        None -> None"""
        # Draw the board
        stroke(*self.BLACK_RGB)
        strokeWeight(2)

        # Draw horizontal lines, skip the edges
        for y in range(100, self.HEIGHT, self.SPACING):
            line(0, y, self.WIDTH, y)

        # Draw vertical lines, skip the edges
        for x in range(100, self.WIDTH, self.SPACING):
            line(x, 0, x, self.HEIGHT)

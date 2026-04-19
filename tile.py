class Tile:
    """A tile."""

    def __init__(self, x, y, color):
        self.SIZE_COEFFICIENT = 0.85
        self.TILE_SIZE = 100 * self.SIZE_COEFFICIENT
        self.WHITE_RGB = (1, 1, 1)
        self.BLACK_RGB = (0, 0, 0)

        self.x = x
        self.y = y
        self.color = color

    def display(self):
        """Draw the tile"""
        noStroke()
        if self.color == "black":
            fill(*self.BLACK_RGB)
        else:
            fill(*self.WHITE_RGB)
        ellipse(self.x, self.y, self.TILE_SIZE, self.TILE_SIZE)

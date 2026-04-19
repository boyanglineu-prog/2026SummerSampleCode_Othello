from game_controller import GameController


def test_diaplay_next_tile():
    gc = GameController(WIDTH=800, HEIGHT=800, SPACING=100)
    spacing = 100
    gc.mouse_tile.display = lambda: None

    test_cases = [
        (0, 0),
        (50, 50),
        (99, 51),
        (199, 342),
        (343, 599),
        (123, 256),
        (399, 399),
    ]
    gc.turn = "black"

    for mouseX, mouseY in test_cases:
        gc.display_next_tile(mouseX, mouseY)

        expected_x = mouseX / spacing * spacing + spacing / 2
        expected_y = mouseY / spacing * spacing + spacing / 2

        assert gc.mouse_tile.x == expected_x
        assert gc.mouse_tile.y == expected_y
        assert gc.mouse_tile.color == "black"

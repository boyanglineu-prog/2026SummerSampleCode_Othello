# Othello Game

A Python-based implementation of the classic board game Othello (also known as Reversi) using Processing. Play against an intelligent AI opponent that strategically selects moves to maximize points.

## Overview

This project implements a fully playable Othello game where a human player (Black) competes against a computer AI (White). The game features:

- **Interactive Gameplay**: Click on the board to place your tiles
- **Intelligent AI**: Computer opponent uses a greedy algorithm to select optimal moves
- **Real-time Scoring**: Live scoreboard shows current tile counts
- **Game State Management**: Automatic detection of valid moves, pass scenarios, and game endings
- **Score Logging**: Game results are saved to a persistent scores file

## Project Structure

### Core Files

- **[game_starter.pyde](game_starter.pyde)**: Main entry point for the Processing sketch. Handles the game loop, rendering, and AI turn timing.

- **[game_controller.py](game_controller.py)**: Manages game state including:
  - Turn management (Black vs White)
  - Score tracking and winner determination
  - Scoreboard display
  - Game result logging to `scores.txt`

- **[tiles.py](tiles.py)**: Core game logic:
  - Tile collection management (2D grid)
  - Legal move calculation
  - Move validation and execution
  - Tile flipping mechanics
  - AI decision making
  - Turn switching and game flow

- **[board.py](board.py)**: Visual board rendering:
  - Draws the 8x8 game grid
  - Handles board display on screen

- **[tile.py](tile.py)**: Individual tile representation:
  - Tile properties (position, color)
  - Tile rendering as circles

### Supporting Files

- **[test_game_controller.py](test_game_controller.py)**: Unit tests for game controller functionality
- **[test_tiles.py](test_tiles.py)**: Unit tests for tile and game logic
- **[scores.txt](scores.txt)**: Persistent file storing game statistics
- **[sketch.properties](sketch.properties)**: Processing sketch configuration

## How to Play

1. **Start the Game**: Run `game_starter.pyde` in Processing (Python mode)

2. **Game Rules**: 
   - The board starts with 4 tiles in the center (2 black, 2 white)
   - Black (player) goes first
   - You can only place tiles that sandwich opponent tiles horizontally, vertically, or diagonally
   - When you place a tile, all opponent tiles between your new tile and existing tiles are flipped
   - If you have no legal moves, your turn is skipped

3. **Making Moves**:
   - Move your mouse to preview your tile placement
   - Click to place a black tile on a valid square
   - The AI (white) automatically plays after your move

4. **Win Condition**:
   - Game ends when neither player has legal moves
   - Player with more tiles wins
   - Results are automatically saved to `scores.txt`

## Game Configuration

Key parameters in `game_starter.pyde`:

```python
WIDTH = 800              # Window width
HEIGHT = 800             # Window height
SPACING = 100            # Grid cell size (8x8 board)
GREEN_RGB = (0, 0.5, 0)  # Board background color
DELAY_TIME = 1250        # AI move delay in milliseconds
```

## AI Strategy

The AI uses a greedy algorithm to select moves:

- Scans all legal moves available
- For each move, calculates how many opponent tiles would be flipped
- Selects the move that captures the most tiles
- This maximizes points per turn

(Note: The current AI strategy is simple and greedy. More advanced strategies like corner control or edge plays could be implemented for stronger performance.)

## Game State Management

- **Legal Moves Dictionary**: Maintains all valid positions and the tiles that would be flipped for each move
- **Turn Switching**: Automatically alternates between player and AI, with pass handling for blocked players
- **Winner Detection**: Tracks when both players have no legal moves and determines the winner
- **Score Logging**: Updates `scores.txt` with game results (total games, player wins, AI wins)

## Testing

The project includes unit tests:

```bash
# Run tests (requires pytest)
pytest test_game_controller.py
pytest test_tiles.py
```

## Requirements

- **Processing** (Java-based, running Python mode)
- **Python 3.x**
- Libraries: Uses Processing's built-in functions (no external pip packages required for main game)

## Future Enhancements

- Implement more advanced AI strategies (minimax, alpha-beta pruning)
- Add difficulty levels
- Implement undo functionality
- Add game statistics and player rankings
- Create a menu system for game options
- Network multiplayer support



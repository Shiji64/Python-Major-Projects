# Tic Tac Toe Game

A simple two-player command-line Tic Tac Toe game developed in Python.

## Project Overview

This project implements the classic Tic Tac Toe game for two players. Player 1 uses `X` and Player 2 uses `O`. Players take turns choosing positions from 1 to 9 on a 3 × 3 board.

The project demonstrates Python functions, loops, conditional statements, lists, dictionaries, tuples, input validation, and exception handling.

## Features Implemented

- Two-player gameplay
- Player 1 uses `X`
- Player 2 uses `O`
- 3 × 3 game board
- Position selection from 1 to 9
- Board display using box-drawing characters
- Row winner checking
- Column winner checking
- Diagonal winner checking
- Draw detection
- Validation for non-numeric input
- Validation for positions outside 1 to 9
- Validation for already occupied positions
- Option to play another round
- Board reset before every new round

## Project File

```text
Tic_Tac_Toe/
|
|-- tic_tac_toe_game.py
|-- README.md
```

## Requirements

- Python 3.x
- No external Python packages are required

## How to Run

1. Keep `tic_tac_toe_game.py` inside the project folder.
2. Open Command Prompt or Terminal inside the folder.
3. Run:

```bash
py tic_tac_toe_game.py
```

You can also use:

```bash
python tic_tac_toe_game.py
```

if `python` is configured on your system.

## Board Positions

Players enter a number from 1 to 9 corresponding to a board position:

```text
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
```

Internally, the program uses a dictionary to map these numbers to row and column positions.

## How to Play

1. The game starts with Player 1 using `X`.
2. Player 1 enters a position from 1 to 9.
3. Player 2 then enters a position using `O`.
4. Players continue taking turns.
5. The game checks for a winner after every valid move.
6. If all positions are filled without a winner, the game is declared a draw.
7. After the game ends, the players can choose whether to play again.

## Winning Conditions

A player wins by placing three matching symbols in:

- Any horizontal row
- Any vertical column
- Either diagonal

## Input Validation

The program handles:

- Non-numeric input
- Numbers below 1
- Numbers above 9
- Positions that are already occupied
- Invalid responses when asked whether to play again

## Main Functions

### `display_board()`

Displays the current Tic Tac Toe board.

### `check_winner(player)`

Checks all rows, columns, and diagonals to determine whether the given player has won.

### `check_draw()`

Checks whether every board position is filled without a winner.

### `reset_board()`

Clears all positions before starting a new round.

### `play_again()`

Asks the players whether they want to start another round.

### `main()`

Controls the complete game loop, player turns, move validation, winner checking, draw checking, and replay option.

## Data Structures Used

The board is stored as a two-dimensional list:

```python
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
```

A dictionary maps the numbers 1 to 9 to board coordinates:

```python
positions = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2)
}
```

The coordinate values are tuples containing the row and column indexes.

## Notes

- The game is designed for two players on the same computer.
- There is no computer/AI opponent in this version.
- The board automatically resets when the players choose to play again.

## Author

Python Project  
Tic Tac Toe Game

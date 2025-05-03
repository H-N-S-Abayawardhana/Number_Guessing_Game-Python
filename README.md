# Number Guessing Game

A simple Python-based number guessing game with multiple difficulty levels.

## Description

This Number Guessing Game is a command-line application where players try to guess a randomly generated number within a specific range. The game offers three difficulty levels, each with different number ranges and maximum attempts.

## Features

- Three difficulty levels: Easy, Medium, and Hard
- Score calculation based on attempts and time taken
- Guess history tracking
- Clean, modular code structure
- User-friendly interface with clear instructions

## How to Run

1. Make sure you have Python 3.6+ installed on your system.
2. Clone or download this repository.
3. Navigate to the project directory in your terminal.
4. Run the game:

```bash
python main.py
```

## Game Rules

1. Choose a difficulty level:
   - **Easy**: Numbers between 1-10, 5 attempts allowed
   - **Medium**: Numbers between 1-50, 10 attempts allowed
   - **Hard**: Numbers between 1-100, 7 attempts allowed

2. Enter your guess when prompted.

3. The game will tell you if your guess is too high or too low.

4. Keep guessing until you find the correct number or run out of attempts.

5. Your score is calculated based on:
   - The difficulty level
   - Number of attempts used
   - Time taken to complete

## Project Structure

```
number_guessing_game/
│
├── main.py                  # Entry point – runs the game
├── game_logic.py            # Handles the core game logic
├── utils.py                 # Utility functions – input validation, formatting
├── config.py                # Game settings – difficulty levels, ranges
├── README.md                # This file
└── requirements.txt         # Dependencies (for future upgrades)
```

## Customizing the Game

### Adding a New Difficulty Level

To add a custom difficulty level, edit the `DIFFICULTY_LEVELS` dictionary in `config.py`:

```python
"extreme": {
    "range": (1, 500),
    "attempts": 5,
    "description": "The ultimate challenge!"
}
```

### Changing Game Parameters

You can modify existing difficulty levels by changing their values in `config.py`.

## Future Improvements

- Add a graphical user interface (GUI) using Tkinter
- Implement sound effects for correct/incorrect guesses
- Add a high-score system with persistent storage
- Create themed versions of the game
- Add hints feature that costs extra points

## Requirements

- Python 3.6 or higher

No external packages are required for the base version of the game.

## License

This project is open-source and available under the MIT License.
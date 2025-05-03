#!/usr/bin/env python3
"""
Number Guessing Game - Main Entry Point
This module serves as the main entry point for the number guessing game.
It handles the user interface and game flow.
"""

import os
import time
from game_logic import GameSession
from config import DIFFICULTY_LEVELS, WELCOME_MESSAGE, GAME_TITLE
import utils


def clear_screen():
    """Clear the terminal screen for better user experience."""
    os.system('cls' if os.name == 'nt' else 'clear')


def display_welcome():
    """Display the welcome message and game title."""
    clear_screen()
    print(GAME_TITLE)
    print("\n" + WELCOME_MESSAGE + "\n")
    time.sleep(1)


def select_difficulty():
    """Allow the user to select a difficulty level."""
    print("\nSelect Difficulty Level:")
    
    for idx, (level, details) in enumerate(DIFFICULTY_LEVELS.items(), 1):
        print(f"{idx}. {level.title()} ({details['range'][0]}-{details['range'][1]}, "
              f"{details['attempts']} attempts)")
    
    while True:
        choice = input("\nEnter your choice (1-3): ")
        if utils.validate_difficulty_choice(choice, len(DIFFICULTY_LEVELS)):
            choice = int(choice)
            # Convert choice to corresponding difficulty key
            difficulty = list(DIFFICULTY_LEVELS.keys())[choice - 1]
            return difficulty
        print("Invalid choice. Please try again.")


def play_game():
    """Main game loop function."""
    display_welcome()
    
    while True:
        difficulty = select_difficulty()
        # Get difficulty settings
        settings = DIFFICULTY_LEVELS[difficulty]
        
        # Create a new game session
        game = GameSession(
            min_num=settings['range'][0],
            max_num=settings['range'][1],
            max_attempts=settings['attempts'],
            difficulty_name=difficulty
        )
        
        clear_screen()
        print(f"\n--- {difficulty.upper()} MODE ---")
        print(f"Guess a number between {settings['range'][0]} and {settings['range'][1]}.")
        print(f"You have {settings['attempts']} attempts.\n")
        
        # Start the game session
        game.play()
        
        # Ask if player wants to play again
        if not utils.play_again():
            break
        clear_screen()
    
    print("\nThanks for playing the Number Guessing Game! Goodbye!")


if __name__ == "__main__":
    try:
        play_game()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Exiting...")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("The game has crashed. Please try again.")
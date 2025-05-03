#!/usr/bin/env python3
"""
Utilities Module
This module contains utility functions for the number guessing game.
"""


def validate_guess(guess_input, min_value, max_value):
    """Validate that the user's guess is a valid integer within the allowed range.
    
    Args:
        guess_input (str): The user's input guess
        min_value (int): Minimum allowed value
        max_value (int): Maximum allowed value
        
    Returns:
        bool: True if the input is valid, False otherwise
    """
    # Check if input is a number
    if not guess_input.strip().isdigit():
        return False
    
    # Convert to integer and check range
    guess = int(guess_input)
    return min_value <= guess <= max_value


def validate_difficulty_choice(choice, num_options):
    """Validate that the user's difficulty choice is valid.
    
    Args:
        choice (str): The user's choice input
        num_options (int): Number of available options
        
    Returns:
        bool: True if the choice is valid, False otherwise
    """
    if not choice.strip().isdigit():
        return False
    
    choice_num = int(choice)
    return 1 <= choice_num <= num_options


def play_again():
    """Ask the user if they want to play again.
    
    Returns:
        bool: True if the user wants to play again, False otherwise
    """
    while True:
        response = input("\nDo you want to play again? (y/n): ").lower().strip()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")
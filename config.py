#!/usr/bin/env python3
"""
Configuration Module
This module contains configuration settings for the number guessing game.
"""

# ASCII art for the game title
GAME_TITLE = """
╔═╗╔╗╔╦ ╦╔╦╗╔╗ ╔═╗╦═╗  ╔═╗╦ ╦╔═╗╔═╗╔═╗╦╔╗╔╔═╗  ╔═╗╔═╗╔╦╗╔═╗
║  ║║║║ ║║║║╠╩╗║╣ ╠╦╝  ║ ╦║ ║║╣ ╚═╗╚═╗║║║║║ ╦  ║ ╦╠═╣║║║║╣ 
╚═╝╝╚╝╚═╝╩ ╩╚═╝╚═╝╩╚═  ╚═╝╚═╝╚═╝╚═╝╚═╝╩╝╚╝╚═╝  ╚═╝╩ ╩╩ ╩╚═╝
"""

# Welcome message displayed at the start of the game
WELCOME_MESSAGE = """
Welcome to the Number Guessing Game!
I'm thinking of a number... Can you guess it?
The faster you guess with fewer attempts, the higher your score will be.
"""

# Difficulty levels with their respective settings
DIFFICULTY_LEVELS = {
    "easy": {
        "range": (1, 10),
        "attempts": 5,
        "description": "Perfect for beginners - a small range of numbers"
    },
    "medium": {
        "range": (1, 50),
        "attempts": 10,
        "description": "A moderate challenge with a larger range"
    },
    "hard": {
        "range": (1, 100),
        "attempts": 7,
        "description": "For those seeking a real challenge"
    }
}

# Optional: Color codes for terminal output
# These can be used with colorama if installed
COLORS = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "magenta": "\033[95m",
    "cyan": "\033[96m",
    "white": "\033[97m",
    "reset": "\033[0m"
}
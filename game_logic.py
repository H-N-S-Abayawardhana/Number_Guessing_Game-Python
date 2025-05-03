#!/usr/bin/env python3
"""
Game Logic Module
This module contains the core logic for the number guessing game.
"""

import random
import time
import utils


class GameSession:
    """Class to manage a single game session."""
    
    def __init__(self, min_num, max_num, max_attempts, difficulty_name):
        """Initialize a new game session with specified parameters.
        
        Args:
            min_num (int): Minimum number in the guessing range
            max_num (int): Maximum number in the guessing range
            max_attempts (int): Maximum number of attempts allowed
            difficulty_name (str): Name of the difficulty level
        """
        self.min_num = min_num
        self.max_num = max_num
        self.max_attempts = max_attempts
        self.difficulty_name = difficulty_name
        self.secret_number = self._generate_number()
        self.attempts = 0
        self.game_won = False
        self.guesses = []
    
    def _generate_number(self):
        """Generate a random number within the specified range.
        
        Returns:
            int: The randomly generated number
        """
        return random.randint(self.min_num, self.max_num)
    
    def check_guess(self, guess):
        """Check if the guess is correct, too high, or too low.
        
        Args:
            guess (int): The player's guess
            
        Returns:
            str: Feedback message indicating if the guess is correct, too high, or too low
        """
        self.attempts += 1
        self.guesses.append(guess)
        
        if guess < self.secret_number:
            return "Too low!"
        elif guess > self.secret_number:
            return "Too high!"
        else:
            self.game_won = True
            return "Correct!"
    
    def play(self):
        """Run the game session, handling user input and game state."""
        start_time = time.time()
        
        while self.attempts < self.max_attempts and not self.game_won:
            # Display attempts information
            attempts_left = self.max_attempts - self.attempts
            print(f"Attempts left: {attempts_left}")
            
            # Get and validate user guess
            user_input = input("Enter your guess: ")
            if not utils.validate_guess(user_input, self.min_num, self.max_num):
                print(f"Please enter a valid number between {self.min_num} and {self.max_num}.")
                continue
            
            guess = int(user_input)
            result = self.check_guess(guess)
            print(f"\n{result}\n")
            
            if self.game_won:
                break
        
        # Calculate game duration
        end_time = time.time()
        duration = round(end_time - start_time, 2)
        
        # Display game results
        self._display_results(duration)
    
    def _display_results(self, duration):
        """Display the final results of the game session.
        
        Args:
            duration (float): Duration of the game in seconds
        """
        if self.game_won:
            print(f"🎉 Congratulations! You guessed the number {self.secret_number} correctly!")
            print(f"It took you {self.attempts} attempt(s) and {duration} seconds.")
            
            # Calculate score based on difficulty, attempts and time
            max_score = self.max_attempts * 100
            time_penalty = min(int(duration) * 2, max_score // 2)
            attempt_bonus = (self.max_attempts - self.attempts + 1) * 50
            score = max(max_score - time_penalty + attempt_bonus, 0)
            
            print(f"Your score: {score} points")
        else:
            print(f"😔 Game over! You've used all {self.max_attempts} attempts.")
            print(f"The secret number was: {self.secret_number}")
        
        # Show guess history
        if len(self.guesses) > 1:
            print("\nYour guesses:", ", ".join(map(str, self.guesses)))
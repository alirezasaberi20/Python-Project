import random

class RockPaperScissors:
    """A class to represent the Rock, Paper, Scissors game. 
    This game is played between a human user and the computer.
    """

    def __init__(self):
        """Initializes the game with a list of possible choices.
        """
        self.choices = ['rock', 'paper', 'scissors']

    def take_computer_choice(self):
        """Randomly selects and returns the computer's choice.
        
        Returns:
            str: The computer's choice from ['rock', 'paper', 'scissors'].
        """
        self.computer_choice = random.choice(self.choices)
        return self.computer_choice

    def take_user_choice(self):
        """Prompts the user to enter a valid choice (rock, paper, or scissors).
        The input is case-insensitive and automatically converted to lowercase.
        
        Returns:
            str: The user's validated choice.
        """
        self.user_choice = input('Enter your choice (Rock/Paper/Scissors): ').lower()

        # Ensure the user enters a valid choice
        if self.user_choice in self.choices:
            return self.user_choice
        # Recursively prompt again if input is invalid
        return self.take_user_choice()

    def decide_winner(self):
        """Determines the winner based on the choices of the user and the computer.

        The game checks if the user wins, loses, or ties with the computer based on 
        pre-defined winning combinations.
        
        Returns:
            str: A message indicating the result of the game (win/lose/tie).
        """
        # Fetch the choices from both the user and computer
        user_choice = self.take_user_choice()
        computer_choice = self.take_computer_choice()

        # Define the winning scenarios where the user beats the computer
        win_combination = [('rock', 'scissors'), ('paper', 'rock'), ('scissors', 'paper')]

        # Check if the user won
        if (user_choice, computer_choice) in win_combination:
            return f"Computer Choice: {self.computer_choice}\nCongrats! You won against the computer!"
        # Check if the game resulted in a tie
        elif user_choice == computer_choice:
            return "It's a tie!"
        # If the user did not win or tie, they lost
        else:
            return f"Computer Choice: {self.computer_choice}\nYou lost!"

if __name__ == '__main__':
    """Main entry point for the Rock, Paper, Scissors game.
    
    The game will continuously loop until the user chooses to quit by pressing 'q'.
    """
    while True:
        # Instantiate a new game object
        game = RockPaperScissors()
        
        # Determine and display the game result
        result = game.decide_winner()
        print(result)
        
        # Prompt the user to play again or quit
        keep_on_game = input('If you want to play again, press any key. To quit, press "q": ')
        
        # Exit the loop and terminate the game if the user chooses to quit
        if keep_on_game.lower() == 'q':
            break

# Number Guessing Game with Statistics

## Challenge

Create a number guessing game where the player attempts to guess a randomly selected number between 1 and 100. The player has 10 tries to guess the number, with feedback provided after each attempt. At the end of the game, a summary of the player’s performance will be displayed.

## Problem Description

### Gameplay
- The program randomly selects a number between 1 and 100.
- The player has 10 attempts to guess the number.
- After each guess, the program will indicate if the guess was:
  - Too high
  - Too low
  - Correct
- Track all guesses made by the player.

### Game End
- If the player guesses the number correctly or uses up all attempts, the game ends.
- Display a summary with:
  - The outcome (win/loss).
  - The total number of guesses made.
  - A list of all guesses.
  - The number of even and odd guesses (using list comprehension).
- Allow the player to restart the game if desired.

## Requirements

- Use a **for loop** to iterate through the 10 attempts.
- Use a **while loop** to ask if the player wants to restart the game.
- Use **if statements** to check if the guess is too high, too low, or correct.
- Use **list comprehension** to filter and display even and odd guesses.

## Example Gameplay

```plaintext
I'm thinking of a number between 1 and 100. You have 10 attempts to guess it.

Attempt 1: 50
Too low!

Attempt 2: 75
Too high!

Attempt 3: 62
Correct! You guessed the number in 3 attempts.
```

### Example Summary

```plaintext
You guessed correctly!
Number of attempts: 3
Your guesses: [50, 75, 62]
Even guesses: [50, 62]
Odd guesses: [75]

Do you want to play again? (yes/no)
```

## Modules Used
- **random**: To generate the number to be guessed.

## Getting Started

To implement this game:
1. Initialize the game with a random number and set attempts to 10.
2. Use a loop to take player input and provide feedback.
3. Track each guess, categorize them as even or odd, and display a summary at the end.
4. Prompt the player to restart or exit the game.

## Found this challenge on Reddit and felt like trying this out
### https://www.reddit.com/r/PythonLearning/comments/1fkix29/comment/lnvx5lt/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
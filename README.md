# Mastermind 4-Color Match Game

Welcome to the **Mastermind 4-Color Match Game**! This is a Python implementation of the classic game Mastermind, where the goal is to guess a secret code within a limited number of tries.

## Features
- Randomly generated secret code using six possible colors.
- User input validation to ensure only valid guesses are entered.
- Feedback after each guess indicating:
  - The number of correct colors in the correct position.
  - The number of correct colors in the wrong position.
- Up to 10 attempts to guess the correct code.

## How to Play
1. The secret code is made up of 4 colors, randomly chosen from the following list:
   `['R', 'G', 'B', 'Y', 'W', 'O']`
2. On each turn, you will input a guess of 4 colors separated by spaces. Example: `R G B Y`
3. After each guess, you will receive feedback:
   - **Correct position**: Number of colors that are in the correct position.
   - **Wrong position**: Number of colors that are correct but in the wrong position.
4. Use the feedback to refine your guesses and try to crack the code within 10 attempts.

## Requirements
- Python 3.6 or higher

## How to Run
1. Clone the repository to your local machine:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd mastermind-4-color-match
   ```
3. Run the game:
   ```bash
   python mastermind.py
   ```

## Code Overview
### Key Constants
- `COLORS`: The list of valid colors (`['R', 'G', 'B', 'Y', 'W', 'O']`).
- `TRIES`: Maximum number of attempts to guess the code (default is 10).
- `CODE_LENGTH`: The length of the secret code (default is 4).

### Functions
1. **`generate_code`**
   - Randomly generates the secret code of 4 colors.

2. **`guess_code`**
   - Prompts the user for their guess, validates the input, and returns the guess as a list.

3. **`check_code`**
   - Compares the user's guess to the secret code.
   - Returns two values:
     - `correct_pos`: Number of colors in the correct position.
     - `incorrect_pos`: Number of correct colors in the wrong position.

4. **`main`**
   - The main function that orchestrates the game logic, including generating the secret code, managing attempts, and providing feedback.

## Example Gameplay
```text
Welcome to mastermind, you have 10 tries to guess the 4 color code.
The valid colors are: R G B Y W O

Enter 4 colors from the following list ['R', 'G', 'B', 'Y', 'W', 'O']: R G B Y
Correct position: 2 || Wrong position: 1

Enter 4 colors from the following list ['R', 'G', 'B', 'Y', 'W', 'O']: R W O Y
Correct position: 1 || Wrong position: 2

...

Congratulations! You have guessed the code in 6 tries.
```

## Contribution
Feel free to fork this repository, create issues, and submit pull requests if you would like to contribute or suggest improvements.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

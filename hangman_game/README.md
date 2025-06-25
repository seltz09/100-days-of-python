# Hangman Game 🎯

A classic word-guessing game built in Python as part of Day 7 of the 100 Days of Python challenge.

## Overview

Test your vocabulary skills by guessing letters to reveal a hidden word! You have 6 lives to figure out the word before the hangman is complete. Each wrong guess brings you one step closer to game over.

## How to Play

1. **Start the game** - Run `main.py` to begin
2. **Guess letters** - Enter one letter at a time when prompted
3. **Track your progress** - Watch as correct letters fill in the blanks
4. **Avoid wrong guesses** - Each incorrect letter costs you a life
5. **Win or lose** - Reveal the entire word to win, or lose all 6 lives and face defeat!

## Game Features

- **200+ challenging words** - From "abruptly" to "zombie"
- **Visual hangman stages** - ASCII art shows your remaining lives
- **Duplicate guess protection** - No penalty for guessing the same letter twice
- **Clear feedback** - Know immediately if your guess was right or wrong
- **Win/lose detection** - Game ends when you complete the word or run out of lives

## File Structure

```
hangman-game/
│
├── main.py           # Main game logic and loop
├── hangman_words.py  # Word list (200+ words)
├── hangman_art.py    # ASCII art for hangman stages and logo
└── README.md         # This file
```

## Requirements

- Python 3.x
- No external libraries required (uses built-in `random` module)

## How to Run

1. Make sure all three Python files are in the same directory
2. Open your terminal/command prompt
3. Navigate to the game directory
4. Run the game:
   ```bash
   python main.py
   ```

## Game Rules

- You start with 6 lives
- Guess one letter at a time
- Correct guesses reveal all instances of that letter in the word
- Wrong guesses cost you one life and advance the hangman drawing
- Repeated guesses don't count against you
- Win by guessing all letters before running out of lives
- Lose if the hangman drawing is completed (0 lives remaining)

## Sample Gameplay

```
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    

Word to guess: _______
You have lives 6 left.
Guess a letter: e
Word to guess: ___e___
```

## Learning Objectives (Day 7)

This project reinforces several key Python concepts:
- **Loops** - `while` loops for game control, `for` loops for string iteration
- **Conditionals** - `if/elif/else` statements for game logic
- **Lists** - Managing word lists and tracking guessed letters
- **String manipulation** - Building display strings and checking characters
- **Imports** - Organizing code across multiple files
- **Random selection** - Using `random.choice()` for word selection

## Possible Enhancements

- Add difficulty levels (word length categories)
- Include hints or word categories
- Track high scores or statistics
- Add multiplayer functionality
- Create a GUI version

---

**Part of 100 Days of Python Challenge - Day 7**

*Built with Python 3 | No external dependencies*

# Python Mini-Projects

**A Collection of Fun, Interactive Python Programs for Beginners!**

Same engaging Python applications that demonstrate fundamental programming concepts through practical examples. From games to utilities, these projects are perfect for learning Python basics while creating usable programs.

**Table of Contents**

1. Project Details
2. Features
3. How to Use
4. Requirements
5. Code Structure
6. References

## Project Details

- **Start Date:** 20/04/2025
- **Last Update:** 20/04/2025
- **Programming Language:** Python 3
- **Tools Used:** VS Code, pip
- **Project Types:** Mini project

## Features

### 🎲 Dice Rolling Simulator

✅ Simple 2-dice roller with random number generation  
✅ User-friendly prompts with input validation  
✅ Continuous play until user exits

### 🔢 Number Guessing Game

✅ Random number generation (1-100)  
✅ "Too high/Too low" feedback system  
✅ Robust error handling for non-numeric inputs

### ✂️ Rock-Paper-Scissors

✅ Emoji visual representation (🪨📄✂️)  
✅ Computer opponent with random choice  
✅ Winner determination logic  
✅ Play-again functionality

### 📲 QR Code Generator

✅ Converts URLs/text to QR codes  
✅ Customizable output (size, colors)  
✅ File saving capability

## How to Use

### Installation

1. Ensure Python 3 is installed
2. For QR Code Generator, install dependencies:
   ```bash
   pip install qrcode
   ```

### Running Programs

Simply execute each Python file:

```bash
python dice_roller.py
python number_guesser.py
python rps_game.py
python qr_generator.py
```

### Usage Guide

**Dice Roller:**

- Press 'y' to roll, 'n' to exit
- See your random dice results

**Number Guesser:**

- Enter numbers between 1-100
- Receive hints until correct guess

**Rock-Paper-Scissors:**

- Choose r (rock), p (paper), or s (scissors)
- See computer's choice and game outcome
- Continue or exit after each round

**QR Generator:**

- Enter text/URL to encode
- Specify output filename
- QR code saves as PNG image

## Requirements

- Python 3.6+
- For QR Generator:
  - qrcode library (`pip install qrcode`)
  - Pillow (auto-installed with qrcode)

## Code Structure

| File                      | Description                                                                   |
| ------------------------- | ----------------------------------------------------------------------------- |
| `dice_rolling_game.py`    | Simple dice simulation with while-loop and random module                      |
| `number_guessing_game.py` | Guessing game with comparison logic and exception handling                    |
| `rock_paper_scissors.py`  | Rock-paper-scissors with emoji visuals, game logic, and user input validation |
| `qr_code_generator.py`    | QR code generation with customizable parameters and file output               |

## References

- [Programming with Mosh](https://www.youtube.com/watch?v=yVl_G-F7m8cab_channel=ProgrammingwithMosh)

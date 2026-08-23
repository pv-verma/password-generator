# password-generator and strength checker 

# Password Toolkit

A command-line Python tool that generates strong, customizable passwords and checks the strength of existing ones — with instant, specific feedback on how to improve them.

## Features

**Password Generator**
- Choose your own length (minimum 8 characters)
- Optionally include uppercase letters, numbers, and special characters
- Lowercase letters are always included as the base character set
- Generate multiple passwords in a row with the same settings

**Password Strength Checker**
- Enter any password and get a strength rating: Weak, Medium, Strong, or Very Strong
- Score is based on 5 criteria: length, uppercase, lowercase, digits, and symbols
- Specific, actionable feedback for whatever criteria are missing (e.g. "Add a number")
- Check multiple passwords in one session

## Getting Started

### Requirements
- Python 3.10 or later
- No external dependencies — built entirely with the standard library (`random`, `string`)

### Installation
```bash
git clone https://github.com/pv-verma/password-generator.git
cd password-generator
```

### Usage
```bash
python password_generator.py
```

You'll be shown a menu to choose between generating a new password or checking an existing one:

```
=== Password Toolkit ===
1. Generate a password
2. Check a password's strength
```

## How It Works

The project is split into small, single-purpose functions so the core logic can be tested independently of user input:

| Function | Purpose |
|---|---|
| `build_character_pool()` | Builds the set of characters available for generation based on selected options |
| `generate_password()` | Randomly generates a password from the character pool |
| `check_criteria()` | Evaluates a password against 5 strength criteria, returning a dict of booleans |
| `calculate_score()` | Converts the criteria dict into a 0–5 score |
| `score_to_label()` | Converts the score into a human-readable strength label |
| `run_generator()` / `run_checker()` | Handle the interactive loop and printed output for each mode |
| `main()` | Displays the menu and routes to the chosen mode |

Keeping the scoring logic (`check_criteria`, `calculate_score`, `score_to_label`) free of any `input()` or `print()` calls made it possible to unit test the strength-checking logic directly, without needing to simulate user input.

## Running Tests

Tests are written with `pytest` and live in `test_password_generator.py`:

```bash
pip install pytest
pytest
```

The test suite covers:
- Character pool construction with different option combinations
- Password length and character-set correctness
- Strength criteria detection on weak and strong example passwords
- Score calculation across all-true, all-false, and mixed criteria
- Score-to-label boundaries (e.g. confirming a score of 3 maps to "Medium")

## Project Structure

```
password-generator/
├── password_generator.py       # Main program: generator, checker, and menu
├── test_password_generator.py  # pytest test suite
└── README.md
```

## Possible Future Improvements

- Save generated passwords to an encrypted local file
- Check passwords against a list of commonly leaked passwords
- Add a password strength "meter" visualization in the terminal

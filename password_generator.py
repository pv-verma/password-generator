import random
import string


def ask_yes_no(question):
    answer = input(question + " (yes/no): ").strip().lower()
    return answer in ("yes", "y")


def ask_length():
    while True:
        raw = input("How long do you want the password to be? ").strip()
        if raw.isdigit() and int(raw) >= 8:
            return int(raw)
        print("Minimum length is 8 characters.\n")


def build_character_pool(use_upper, use_numbers, use_symbols):
    pool = ""
    # lowercase is always included as the base
    pool += string.ascii_lowercase
    if use_upper:
        pool += string.ascii_uppercase
    if use_numbers:
        pool += string.digits
    if use_symbols:
        pool += "!@#$%"
    return pool


def generate_password(length, pool):
    return "".join(random.choice(pool) for _ in range(length))


def check_criteria(password):
    """Return a dict showing which strength criteria a password meets."""
    return {
        "length_ok": len(password) >= 8,
        "has_upper": any(char.isupper() for char in password),
        "has_lower": any(char.islower() for char in password),
        "has_digit": any(char.isdigit() for char in password),
        "has_symbol": any(char in "!@#$%^&*()-_=+[]{};:,.<>?/" for char in password),
    }


def calculate_score(criteria):
    """Count how many strength criteria were met, out of 5."""
    return sum(criteria.values())


def score_to_label(score):
    """Convert a 0-5 score into a human-readable strength label."""
    if score <= 2:
        return "Weak"
    elif score == 3:
        return "Medium"
    elif score == 4:
        return "Strong"
    else:
        return "Very Strong"


def run_generator():
    print("\n=== Password Generator ===\n")

    length = ask_length()
    use_upper = ask_yes_no("Include uppercase letters?")
    use_numbers = ask_yes_no("Include numbers?")
    use_symbols = ask_yes_no("Include special characters like !@#$%?")

    if not use_upper and not use_numbers and not use_symbols:
        print("\nYou need to pick at least one option besides lowercase!")
        return

    pool = build_character_pool(use_upper, use_numbers, use_symbols)

    while True:
        password = generate_password(length, pool)
        print(f"\nGenerated password: {password}")

        if not ask_yes_no("\nGenerate another password with the same settings?"):
            print("\nDone! Keep your passwords safe.")
            break


def run_checker():
    print("\n=== Password Strength Checker ===\n")

    while True:
        password = input("Enter a password to check: ")
        criteria = check_criteria(password)
        score = calculate_score(criteria)
        label = score_to_label(score)

        print(f"\nStrength: {label} ({score}/5 criteria met)")
        if not criteria["length_ok"]:
            print("- Use at least 8 characters")
        if not criteria["has_upper"]:
            print("- Add an uppercase letter")
        if not criteria["has_lower"]:
            print("- Add a lowercase letter")
        if not criteria["has_digit"]:
            print("- Add a number")
        if not criteria["has_symbol"]:
            print("- Add a special character (e.g. !@#$%)")

        if not ask_yes_no("\nCheck another password?"):
            print("\nDone!")
            break


def main():
    print("=== Password Toolkit ===")
    print("1. Generate a password")
    print("2. Check a password's strength")

    while True:
        choice = input("\nChoose an option (1 or 2): ").strip()
        if choice == "1":
            run_generator()
            break
        elif choice == "2":
            run_checker()
            break
        else:
            print("Please enter 1 or 2.")


if __name__ == "__main__":
    main()
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


def main():
    print("=== Password Generator ===\n")

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


if __name__ == "__main__":
    main()
import re
import secrets
import string

"""
Generates a secure random password with customizable constraints.

Parameters:
- length (int, optional): The length of the password. Default is 16.
- nums (int, optional): The minimum number of digits required. Default is 1.
- special_chars (int, optional): The minimum number of special characters required. Default is 1.
- uppercase (int, optional): The minimum number of uppercase letters required. Default is 1.
- lowercase (int, optional): The minimum number of lowercase letters required. Default is 1.

Returns:
- str: A randomly generated password that meets the specified constraints.

Algorithm:
1. Define the pool of possible characters (letters, digits, and symbols).
2. Generate a password by randomly selecting characters from the pool.
3. Validate the password against the specified constraints using regex.
4. Repeat the process until a valid password is generated.

Example:
    new_password = generate_password(length=12, nums=2, special_chars=2, uppercase=2, lowercase=2)
    # Output: A password like "A1b@C2d#E3f$"
"""


def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):

    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ""
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)

        constraints = [
            (nums, r"\d"),
            (special_chars, rf"[{symbols}]"),
            (uppercase, r"[A-Z]"),
            (lowercase, r"[a-z]"),
        ]

        # Check constraints
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break

    return password


if __name__ == "__main__":
    new_password = generate_password()
    print("Generated password:", new_password)

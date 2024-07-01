import random

def get_user_input(prompt, valid_responses=None):
    while True:
        response = input(prompt).lower()
        if valid_responses and response not in valid_responses:
            print(f"Invalid input. Please enter one of the following: {', '.join(valid_responses)}")
        else:
            return response

def passwordGen():
    print("Enter Password Length (length should be less than 74):")
    while True:
        try:
            length = int(input())
            if length >= 75:
                print("Length should be less than 74. Please try again:")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number:")

    symbol = get_user_input("Include symbols (!@#$%^&*)? (Type y or n):", ['y', 'n'])
    number = get_user_input("Include numbers (0-9)? (Type y or n):", ['y', 'n'])
    upper = get_user_input("Include uppercase letters (A-Z)? (Type y or n):", ['y', 'n'])
    lower = get_user_input("Include lowercase letters (a-z)? (Type y or n):", ['y', 'n'])
    special = get_user_input("Include special characters (_-+=)? (Type y or n):", ['y', 'n'])
    exclude = get_user_input("Exclude same character (y or n):", ['y', 'n'])

    charset = ""
    if symbol == 'y':
        charset += "!@#$%^&*"
    if number == 'y':
        charset += "0123456789"
    if upper == 'y':
        charset += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if lower == 'y':
        charset += "abcdefghijklmnopqrstuvwxyz"
    if special == 'y':
        charset += "_-+="

    if not charset:
        print("No character set selected. Please run the program again and select at least one character set.")
        return

    if exclude == 'y' and length > len(charset):
        print("Password length exceeds the number of unique characters available. Please reduce the length or include more character types.")
        return

    password = ""
    if exclude == 'y':
        used_chars = set()
        while len(password) < length:
            val = random.choice(charset)
            if val not in used_chars:
                password += val
                used_chars.add(val)
    else:
        for _ in range(length):
            password += random.choice(charset)
    
    print("Generated password:", password)

if __name__ == "__main__":
    passwordGen()

import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols, avoid_similar):
    # Define character sets
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase
    digit_chars = string.digits
    symbol_chars = string.punctuation if use_symbols else ''

    # Remove similar characters like 'l', 'I', '1', 'O', '0' if needed
    if avoid_similar:
        lowercase_chars = lowercase_chars.replace('l', '').replace('o', '')
        uppercase_chars = uppercase_chars.replace('I', '').replace('O', '')
        digit_chars = digit_chars.replace('1', '9').replace('0', '8')

    # Create a character set based on user preferences
    character_set = ''
    if use_uppercase:
        character_set += uppercase_chars
    if use_lowercase:
        character_set += lowercase_chars
    if use_digits:
        character_set += digit_chars
    if use_symbols:
        character_set += symbol_chars

    # Check if there's at least one character type selected
    if not character_set:
        return "Please select at least one character type."

    # Generate the password
    password = ''.join(random.choice(character_set) for _ in range(length))
    return password

def main():
    print("Random Password Generator")
    print("-------------------------")

    try:
        length = int(input("Enter the password length: "))
        use_uppercase = input("Include uppercase letters (Y/N): ").strip().lower() == 'y'
        use_lowercase = input("Include lowercase letters (Y/N): ").strip().lower() == 'y'
        use_digits = input("Include digits (Y/N): ").strip().lower() == 'y'
        use_symbols = input("Include symbols (Y/N): ").strip().lower() == 'y'
        avoid_similar = input("Avoid similar characters (Y/N): ").strip().lower() == 'y'

        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols, avoid_similar)

        print("\nGenerated Password:")
        print(password)

    except ValueError:
        print("Invalid input. Please enter a valid number for password length.")

if __name__ == "__main__":
    main()

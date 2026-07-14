import random
import string

def generate_password(length, use_uppercase, use_numbers, use_special):
    # Base character set (lowercase is always included)
    char_pool = string.ascii_lowercase
    
    if use_uppercase:
        char_pool += string.ascii_uppercase
    if use_numbers:
        char_pool += string.digits
    if use_special:
        char_pool += string.punctuation

    # If the pool is somehow empty (should not happen as lowercase is default)
    if not char_pool:
        return "Error: No characters selected."

    # Generate random password from the pool
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

def main():
    print("=========================================")
    print("       🔑 SECURE PASSWORD GENERATOR      ")
    print("=========================================\n")
    
    # 1. Get password length with validation
    while True:
        try:
            length = int(input("Enter desired password length (minimum 6): "))
            if length < 6:
                print("❌ Password should be at least 6 characters long for security.")
                continue
            break
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

    # 2. Get user preferences
    print("\nCustomize your password settings:")
    use_uppercase = input("Include Uppercase letters? (y/n): ").strip().lower() == 'y'
    use_numbers = input("Include Numbers? (y/n): ").strip().lower() == 'y'
    use_special = input("Include Special characters? (y/n): ").strip().lower() == 'y'

    # 3. Generate and display password
    password = generate_password(length, use_uppercase, use_numbers, use_special)
    
    print("\n-----------------------------------------")
    print(f"🔒 Your Generated Password is: {password}")
    print("-----------------------------------------")
    print("Keep it safe and secure!")

if __name__ == "__main__":
    main()
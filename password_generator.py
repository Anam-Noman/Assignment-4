import random
import string

def generate_password(length):
    """Generate a random password with a given length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!")
    
    # Get user input for number of passwords and password length
    num_passwords = int(input("How many passwords would you like to generate? "))
    password_length = int(input("Enter the length of each password: "))

    print("\nHere are your random passwords:")

    # Generate and display the passwords
    for _ in range(num_passwords):
        print(generate_password(password_length))

# Start the password generator
main()

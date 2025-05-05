import random

def user_guess_game():
    print("🎮 Welcome to the 'Guess the Number' game!")
    print("I'm thinking of a number between 1 and 100.")
    print("_"*50)
    
    number = random.randint(1, 100)  # Computer picks a random number
    attempts = 0

    while True:
        try:
            guess = int(input("🔢 Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("⚠️ Please enter a number between 1 and 100.")
            elif guess < number:
                print("📉 Too low! Try a higher number.")
            elif guess > number:
                print("📈 Too high! Try a lower number.")
            else:
                print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
                break

        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")

# Start the game
user_guess_game()

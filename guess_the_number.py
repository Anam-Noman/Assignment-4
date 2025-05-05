import random

def computer_guess_game():
    print("🎯 Think of a number between 1 and 100 (the computer will try to guess it).")
    input("✅ Press 'Enter' when you're ready...")

    low = 1
    high = 100
    attempts = 0

    while True:
        # Computer makes a guess
        guess = random.randint(low, high)
        attempts += 1

        print(f"\n🤖 Computer's guess: {guess}")
        print("Please respond with:")
        print("  [H] -> If the guess is too High")
        print("  [L] -> If the guess is too Low")
        print("  [C] -> If the guess is Correct")

        feedback = input("➡️  Your response (H/L/C): ").strip().lower()

        # Adjust the range based on feedback
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback == 'c':
            print(f"\n🎉 The computer guessed your number in {attempts} attempts!")
            break
        else:
            print("⚠️  Invalid input! Please enter only H, L, or C.")

# Start the game
computer_guess_game()

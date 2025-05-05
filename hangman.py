import random
import string

def get_valid_word(word_list):
    word = random.choice(word_list)
    while '-' in word or ' ' in word:
        word = random.choice(word_list)
    return word.upper()

def hangman():
    words = ["python", "typescript", "keyboard", "monitor", "hangman", "developer", "project"]
    word = get_valid_word(words)
    word_letters = set(word)  # Letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # Letters guessed by the user

    lives = 6

    print("🎯 Welcome to Hangman!")
    
    while len(word_letters) > 0 and lives > 0:
        # Show lives and used letters
        print(f"\n💡 You have {lives} lives left. Used letters: {' '.join(sorted(used_letters))}")
        
        # Display current word status
        word_display = [letter if letter in used_letters else '_' for letter in word]
        print("🔠 Word: ", ' '.join(word_display))

        # Get user input
        user_letter = input("📨 Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("✅ Correct!")
            else:
                lives -= 1
                print("❌ Wrong guess.")
        elif user_letter in used_letters:
            print("⚠️ You already used that letter. Try again.")
        else:
            print("🚫 Invalid character. Please guess a letter.")

    # Game over messages
    if lives == 0:
        print(f"\n💀 You died! The word was {word}")
    else:
        print(f"\n🎉 Congratulations! You guessed the word: {word}")

# Start the game
hangman()

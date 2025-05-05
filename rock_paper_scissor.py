import random

def play():
    print("🎮 Let's play Rock, Paper, Scissors!")
    user = input("Choose one: rock, paper, or scissors ➡️ ").lower()
    computer = random.choice(['rock', 'paper', 'scissors'])

    print(f"\n🧑 You chose: {user}")
    print(f"🤖 Computer chose: {computer}")

    if user == computer:
        return "🤝 It's a tie!"

    # Winning conditions for user
    if is_win(user, computer):
        return "🎉 You win!"
    
    return "😢 You lose."

def is_win(player, opponent):
    # Return True if player beats opponent
    return (
        (player == 'rock' and opponent == 'scissors') or
        (player == 'scissors' and opponent == 'paper') or
        (player == 'paper' and opponent == 'rock')
    )

# Play the game
print(play())

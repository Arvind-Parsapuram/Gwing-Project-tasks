# Paste your game code here
import random

def rock_paper_scissors():
    print("✊ 🖐 ✌ Welcome to Rock, Paper, Scissors!")
    choices = ["rock", "paper", "scissors"]
    user_wins = 0
    computer_wins = 0
    rounds_played = 0

    while True:
        print("\nType 'rock', 'paper', or 'scissors' to play. Type 'exit' to quit.")
        user_choice = input("Your choice: ").lower()

        if user_choice == "exit":
            print("\nGame Over!")
            print(f"🏁 Total Rounds Played: {rounds_played}")
            print(f"😎 Your Wins: {user_wins}")
            print(f"🤖 Computer Wins: {computer_wins}")
            break

        if user_choice not in choices:
            print("⚠ Invalid choice. Please try again.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        rounds_played += 1

        if user_choice == computer_choice:
            print("It's a draw! 🤝")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win this round! 🎉")
            user_wins += 1
        else:
            print("Computer wins this round! 💻")
            computer_wins += 1

# Run the game
rock_paper_scissors()

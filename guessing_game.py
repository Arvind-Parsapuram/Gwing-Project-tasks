import random

def number_guessing_game():
    print("🎲 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    total_games = 0
    total_wins = 0

    while True:
        # Choose difficulty
        print("\nSelect Difficulty:")
        print("1. Easy (10 attempts)")
        print("2. Medium (7 attempts)")
        print("3. Hard (5 attempts)")

        difficulty = input("Enter choice (1/2/3): ").strip()
        if difficulty == '1':
            max_attempts = 10
        elif difficulty == '2':
            max_attempts = 7
        elif difficulty == '3':
            max_attempts = 5
        else:
            print("⚠ Invalid choice. Defaulting to Easy mode.")
            max_attempts = 10

        secret_number = random.randint(1, 100)
        attempts = 0
        previous_diff = None
        won = False

        print(f"\n🎯 You have {max_attempts} attempts. Let's begin!")

        while attempts < max_attempts:
            try:
                guess = int(input(f"Attempt {attempts+1}/{max_attempts} - Enter your guess: "))
                attempts += 1

                if guess < 1 or guess > 100:
                    print("⚠ Please guess a number between 1 and 100.")
                    continue

                diff = abs(secret_number - guess)

                if guess < secret_number:
                    print("Too low! 🔽")
                elif guess > secret_number:
                    print("Too high! 🔼")
                else:
                    print(f"🎉 Correct! You guessed it in {attempts} attempts.")
                    won = True
                    total_wins += 1
                    break

                # Hint: getting warmer or colder
                if previous_diff is not None:
                    if diff < previous_diff:
                        print("🔥 Warmer!")
                    elif diff > previous_diff:
                        print("❄️ Colder!")
                    else:
                        print("😐 Same distance as before.")
                previous_diff = diff

            except ValueError:
                print("⚠ Invalid input. Please enter a number.")

        total_games += 1

        if not won:
            print(f"❌ Out of attempts! The correct number was {secret_number}.")

        # Show score
        print(f"\n📊 Score: {total_wins} wins out of {total_games} games.")

        # Ask to play again
        play_again = input("🔁 Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("👋 Thanks for playing! Goodbye.")
            break

# Run the game
number_guessing_game()

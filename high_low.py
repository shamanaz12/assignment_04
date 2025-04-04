import random

# Constants
NUM_ROUNDS = 5  # Number of rounds in the game

def play_round(round_number):
    # Generate a random number for the computer and the player
    computer_number = random.randint(1, 100)
    player_number = random.randint(1, 100)

    print(f"Round {round_number}")
    print(f"Your number is {player_number}")

    # Get player's guess
    guess = input("Do you think your number is higher or lower than the computer's?: ").lower()

    # Check if the guess is correct
    if guess not in ['higher', 'lower']:
        print("Invalid input! Please type 'higher' or 'lower'.")
        return 0  # No score for invalid input

    # Check if the player's guess matches the truth
    if (guess == "higher" and player_number > computer_number) or (guess == "lower" and player_number < computer_number):
        print(f"You were right! The computer's number was {computer_number}")
        return 1
    elif player_number == computer_number:
        print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        return 0
    else:
        print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        return 0

def main():
    score = 0

    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    # Play multiple rounds
    for round_number in range(1, NUM_ROUNDS + 1):
        score += play_round(round_number)
        print(f"Your score is now {score}\n")

    # Print final score
    print(f"Thanks for playing! Your final score is: {score}")
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    main()

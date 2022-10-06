import random

computer_score = 0
user_score = 0
i = 0
chance = int(input("How manys time you want to play (no. of chances)?: "))

while i <= chance:

    user_input = input("\nPick Rock, Paper, or Scissors: ").lower()

    possible_options = ["Rock", "Paper", "Scissors"]
    computer_option = random.choice(possible_options).lower()

    if user_input == computer_option:
        print("You both tied!")
    elif user_input == "rock":
        if computer_option == "scissors":
            user_score += 1
            print("Rock smashes Scissors! You win!")
        else:
            computer_score += 1
            print("Paper covers rock! You lose.")
    elif user_input == "paper":
        if computer_option == "rock":
            user_score += 1
            print("Paper convers rock! You win.")
        else:
            computer_score += 1
            print("Scissors cuts paper! You lose.")
    elif user_input == "scissors":
        if computer_option == "paper":
            user_score += 1
            print("Scissors cuts paper! You win!")
        else:
            computer_score += 1
            print("Rock smashes scissors! You lose.")

    print(
        f"You chose {user_input} - Points: {user_score}, computer chose {computer_option} - Points: {computer_score}.\n")
    
    play_again = input("Want to play again: (y/n) ")
    if play_again.lower() != 'y':
        break

    i += 1
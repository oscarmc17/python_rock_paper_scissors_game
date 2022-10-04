import random

# user_input = input("Let's play rock, paper, and scissors. Yes? Y/N ")
user_input = input("Pick rock, paper, or scissors: ")

# if user_input.lower() == 'y':
#     print("Okay, here we go. ")
# else:
#     print("You don't want to play? ")

possible_options = ["Rock", "Paper", "Scissors"]
computer_option = random.choice(possible_options)

# start = input("You'll play against a computer. Pick first: ")
print(f"\nYou chose {user_input}, computer chose {computer_option}.\n")

if user_input == computer_option:
    print(f"Both players selected {user_input}. It's a tie!")
elif user_input == "rock":
    if computer_option == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_input == "paper":
    if computer_option == "rock":
        print("Paper convers rock! You win.")
    else:
        print("Scissors cuts paper! You lose.")
elif user_input == "Scissors":
    if computer_option == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
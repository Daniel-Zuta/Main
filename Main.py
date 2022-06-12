import random

while True:
    user_choice = input("Enter a choice (r for rock, p for paper and s for scissors): ")
    
    possible_choices = ["r", "p", "s"]
    
    computer_choice = random.choice(possible_choices)
    
    print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")
    
    if user_choice== computer_choice:
        print(f"Both players selected {user_choice}. It's a tie!")
    
    elif user_choice == "r":
        if computer_choice == "s":
            print("You chose scissors! You win!")
        else:
            print("You chose rock! You lose.")
    elif user_choice == "p":
        if computer_choice == "r":
            print("You chose rock! You win!")
        else:
            print("You chose paper! You lose.")
    elif user_choice == "s":
        if computer_choice == "p":
            print("You win!")
        else:
            print("Rock smashes scissors! You lose.")
    play_again = input("play again? (y/n): ")
    if play_again.lower() != "y":
        print('Goodbye')
        break 



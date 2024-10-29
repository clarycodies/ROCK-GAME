import random

game_images = [
    '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
    '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',
    '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
]

def print_game_image(image):
    print(image)

def get_user_choice():
    while True:
        try:
            user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
            if user_choice in [0, 1, 2]:
                return user_choice
            else:
                print("You typed an invalid number, please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_computer_choice():
    return random.randint(0, 2)

def determine_winner(user_choice, computer_choice):
    if user_choice == (computer_choice - 1) % 3:
        return "You win!"
    elif computer_choice == (user_choice - 1) % 3:
        return "You lose!"
    else:
        return "It's a draw!"

def play_game():
    user_choice = get_user_choice()
    print_game_image(game_images[user_choice])

    computer_choice = get_computer_choice()
    print("Computer chose:")
    print_game_image(game_images[computer_choice])

    result = determine_winner(user_choice, computer_choice)
    print(result)

def main():
    play_again = "yes"
    while play_again.lower() == "yes":
        play_game()
        while True:
            play_again = input("Do you want to play again? Type 'yes' or 'no'.\n").strip().lower()
            if play_again in ["yes", "no"]:
                break
            else:
                print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
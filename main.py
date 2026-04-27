from menu import menu
from user import get_user_choice
from computer import computer_choice
from logic import decide_winner

def play_game():
    user = get_user_choice()
    computer = computer_choice()

    print("\nUSER CHOICE:", user)
    print("COMPUTER CHOICE:", computer)
    print("RESULT:", decide_winner(user, computer))

while True:
    menu()
    option = int(input("Enter your option: "))

    if option == 1:
        play_game()
    elif option == 2:
        print("Thank you for playing!")
        break
    else:
        print("Invalid option! Try again.")
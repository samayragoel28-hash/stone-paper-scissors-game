def get_user_choice():
    print("\nChoose one:")
    print("1. STONE")
    print("2. PAPER")
    print("3. SCISSORS")

    choice = int(input("Enter your choice (1-3): "))

    if choice == 1:
        return "STONE"
    elif choice == 2:
        return "PAPER"
    elif choice == 3:
        return "SCISSORS"
    else:
        print("Invalid choice!")
        return get_user_choice()
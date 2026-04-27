def decide_winner(user, computer):
    if user == computer:
        return "DRAW"
    elif (user == "STONE" and computer == "SCISSORS") or \
         (user == "PAPER" and computer == "STONE") or \
         (user == "SCISSORS" and computer == "PAPER"):
        return "YOU WIN!"
    else:
        return "COMPUTER WINS!"
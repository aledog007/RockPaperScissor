import random

choices = ("r", "p", "s")
cPoints = 0
pPoints = 0


def player():
    global choices
    symbols = input(
        "Choose either rock(r), paper(p), or scissors(s).\nYour input: "
    ).lower()

    if symbols not in choices:
        print("You did not enter a valid option. ")
        return player()
    else:
        return symbols


def computer():
    return random.choice(choices)


def game():
    global cPoints, pPoints
    pChoice = player()
    cChoice = computer()

    print("The Computer has chosen: ", cChoice)
    print("You have chosen: ", pChoice)

    if pChoice == cChoice:
        print("\nIt's a tie! No one gets a point.")
    elif (
        (pChoice == "r" and cChoice == "s")
        or (pChoice == "s" and cChoice == "p")
        or (pChoice == "p" and cChoice == "r")
    ):
        print("\nYou won!")
        pPoints += 1
    else:
        print("\nComputer has won!")
        cPoints += 1

    print("")


print("Welcome to the funny Rock Paper and Scissors game! 😎")
while True:
    for i in range(5):
        game()

    print("Your score is:", pPoints, "!\nMy Score is:", cPoints, "!")
    print()

    again = int(
        input("Press 1 to continue\nPress 2 to reset and continue\nPress 3 to exit\n")
    )

    if again == 1:
        continue
    elif again == 2:
        pPoints = 0
        cPoints = 0
    elif again == 3:
        break

print("Ok! Bye!")

import random


def rock():
    if userChoice == "Roche":
        print("It's a draw")
    elif userChoice == "Scissors":
        print("You lost")
    elif userChoice == "Paper":
        print("You win")

def scissors():
    if userChoice == "Rock":
        print("You won")
    elif userChoice == "Scissors":
        print("It's a draw")
    elif userChoice == "Paper":
        print("You lost")

def paper():
    if userChoice == "Rock":
        print("You lost")
    elif userChoice== "Scissors":
        print("You won")
    elif userChoice == "Paper":
        print("It's a draw")


userChoice = input("Rock, Paper or Scissor? ")

res = random.randrange(1, 3)

if res == 1:
    rock()
elif res == 2:
    paper()
elif res == 3:
    scissors()




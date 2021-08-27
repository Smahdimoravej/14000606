import random

while 1:
    def match():
        user = input("plaese insert between rock & papaer & scissors: ")
        player = ""
        number = random.randint(1, 3)
        if number == 1:
            player = "rock"
            print("player choises rock")
        elif number == 2:
            player = "paper"
            print("player choises paper")
        elif number == 3:
            player = "scissors"
            print("player choises scissors")

        if user == player:
            print(" = ")
        if user == "rock" and player == "paper":
            print("you lost")
        if user == "rock" and player == "scissors":
            print("you win")
        if user == "paper" and player == "scissors":
            print("you lost")
        if user == "paper" and player == "rock":
            print("you win")
        if user == "scissors" and player == "rock":
            print("you lost")
        if user == "scissors" and player == "paper":
            print("you win")


match()

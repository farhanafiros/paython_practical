import random

def get_computer_choices():
    choice = ["rock","paper", "scissors"]
    return random.choices(choice)

def get_player_choice():
    choices =(input("enter your choice:"))
    print(choices)
def check_winner(player,computer):
    if player == computer:
        print("draw")
    elif (player == "rock" and computer == "scissors"):
        print("player win")
    elif (player == "scissors" and computer == "paper"):
        print("player win")
    elif (player == "paper" and computer == "rock"):
        print("player win")
    else :
        print("copmuter win")

def paly_game():
    choice = get_computer_choices()
    print (choice)
    choices = get_player_choice()
    print (choices)
    check_winner(choices,choice)
paly_game()



    





    
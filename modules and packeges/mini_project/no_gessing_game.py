import random

def genarate_number():
    number = random.randint(1,100)
    return number
    

def get_guess():
    guess = int(input("ente your guess:"))
    return guess
        

def check_guess(guess,number):
    if guess > number :
        print("to high")
    elif guess < number:
        print("to low")
    elif guess == number:
        print("correct")

def play_game():
    number = genarate_number()
    print(number)
    guess = get_guess()
    check_guess(guess,number)

play_game()

       



        


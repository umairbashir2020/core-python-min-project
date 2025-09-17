"""
1 - input from the user 
2- computer choice (computer will choose randomly not conditionally)
3- Result print


Papr -rock - scissor (compare)

Cases:
A - Paper
paper - paper = tie
paper - rock = paper win
paper - scissor = scissor win

B - Rock
rock - rock = tie
rock - paper = paper win
rock - scissor = rock win

C - Scissor
scissor - scissor = tie
scissor - paper = scissor win
scissor - rock = rock win

"""

import random

item_list = ['rock', 'paper', 'scissor']
user_choice = input("Enter your move = Rock - Paper - Scissor = ")
computer_choice =  random.choice(item_list)

print(f"User choice = {user_choice} , computer choice = {computer_choice}")

if user_choice == computer_choice:
    print('Both chooses same, math tie')

elif user_choice == "rock":
    if computer_choice =="paper":
        print('paper covers rock - paper - computer wins')
    else:
        print("rock smashed scissor - you wins ")

elif user_choice == 'paper':
    if computer_choice == 'scissor':
        print("scissor cuts the paper - computer win ")
    else:
        print('paper covers rock - you win')

elif user_choice == 'scissor':
    if computer_choice == "paper" :
        print('scissor cuts the paper - you wins')
    else:
        print('rock smashes scissor - computer wins')
        







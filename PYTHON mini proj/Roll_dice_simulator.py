# It will print a roll dice for X number of dices with Y number of faces
#took me like half an hour i guess

import random
from typing import Optional


def dice_generator(DICE_FACES):
    dice_number = random.randint(1,DICE_FACES)

    return dice_number
#returns a random number to represent the face of the dice that landed on

def multiple_dice(NUM_OF_DICE,DICE_FACES):

    dices = []
    for i in range(NUM_OF_DICE):
        dice_number = dice_generator(DICE_FACES)
        dices.append(dice_number)
    
    return dices
# it creates a list of random dices to store it to be able stack there any dice that the user wants because he may want more dices

def menu():
    print("How many dices you want to roll?")
    NUM_OF_DICE = int(input())
    print("How many faces do you want the dice to have?")
    DICE_FACES = int(input())

    return NUM_OF_DICE, DICE_FACES
#promps the user to chose the type of dices: number of faces a dice has and how many he wants to throw


def printing_dices(dices,NUM_OF_DICE):
    for i in range(NUM_OF_DICE):
        print("Dice no " + str(i + 1) + ": " + str(dices[i]))

#just standard print for every dice

def start():
    NUM_OF_DICE, DICE_FACES = menu()
    dice_number = dice_generator(DICE_FACES)
    dices = multiple_dice(NUM_OF_DICE,DICE_FACES)
    printing_dices(dices,NUM_OF_DICE)

    return NUM_OF_DICE,DICE_FACES,dices
#combining everything into one start function


def restart(DICE_FACES,NUM_OF_DICE):
    dice_number = dice_generator(DICE_FACES)
    dices = multiple_dice(NUM_OF_DICE,DICE_FACES)
    printing_dices(dices,NUM_OF_DICE)

# its the same as start but its missing the part where asks the user for the num and type of dice

def menu_options():
    print("")
    print("1.Try again with the same dices?")
    print("2.Change the dices?")
    print("3.Exit")
    option = int(input())
    
    return option
# asks t he user if he wants to paly again or change something, nothing improtant


def games_menu():
    choice = 1
    NUM_OF_DICE,DICE_FACES,dices = start()
    choice = menu_options()
    while choice !=3:
        if choice == 1:
            restart(DICE_FACES,NUM_OF_DICE)
            choice = menu_options()
        if choice == 2:
            start()
            choice = menu_options()
        if choice == 3:
            break

#just a loop for the user to continue to paly the game untill he changes his mind

games_menu()
#the start of the domino
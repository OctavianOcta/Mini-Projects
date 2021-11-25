#computer picks a number and you have to guess it basically on easy mode, play it and you ll see why
import random


def computer_pick(min, max):
    pc_choice = random.randint(min,max)

    return pc_choice

def setting_min_max():
    print("Please set the minimum no for the range.")
    min = int(input())
    print("Please set the maximum no for the range.")
    max = int(input())

    return min, max

def picking():
    pl_choice = int(input("Your guess: "))

    return pl_choice

def menu():
    tries = 1
    min,max = setting_min_max()
    pc_choice = computer_pick(min,max)
    print("Computer already chose the number. Try guessing.")
    pl_choice = pc_choice - 1


    min_r = min
    max_r = max


    while pl_choice != pc_choice:
        
        range = (min_r,max_r)
        print("Your range now is: ")
        print("")
        print(range)
        pl_choice = picking()


        if pl_choice < pc_choice:
            print("Your number is too low.")
            min_r = pl_choice


        if pl_choice > pc_choice:
            print("Your number is too high.")
            max_r = pl_choice


        if pl_choice == pc_choice:
            print("Congrats! You guessed it in " + str(tries) + " guesses.")
            print("Wanan try again?")
            print("1. Yes  2. No")
            
            try_again = int(input())
            
            if try_again == 1:
                menu()
            else:
                break
        tries +=1 
    
menu()
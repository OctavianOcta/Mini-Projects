#generate a password made out of random characcters
import string
import random

CHR = list(string.ascii_letters + string.digits)

def length_setting():
    print("How many characters do you want your password to have?")
    len = int(input())

    return len

def password_generator(len, CHR):
    password = ""
    for i in range(len):
        character = random.choice(CHR)
        password += character
    
    return password

def password_showing(pwd):
    print("Your generated password now is: ")
    print("-" * 10)
    print(pwd)
    print("_" * 10)

def start():
    len = length_setting()
    password = password_generator(len,CHR)
    password_showing(password)

start()
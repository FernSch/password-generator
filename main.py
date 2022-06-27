###
#
#   Based off of https://github.com/durzal1/password-generator-/blob/master/number.py but made in console
#   I added the requirment that the password must have a number in it since most do
#   This runs a check to make sure the password has a number in it. if not, it regenerates it
#
###

import random

#length = input("How long do you want your password to be? (must be at least 7 characters): ")

def make_pass(length):

    characters = [1, 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 0 , 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p','a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'E', 'R', 'T','Y', 'U', 'I','O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']

    password = " "
    num_in_pass = False

    if length < 7 or length > 21:
        raise Exception("Password must be between 7 and 21 characters")

#check for number in password
    while num_in_pass == False:
        for i in range(length):
            choice = random.choice(characters)
            if type(choice) == int:
                num_in_pass = True
            password += str(choice)
        if num_in_pass:
            break
    
    return password


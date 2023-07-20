#Berkiel Molinard
#1095255
#Homework 2 problem set 1
#this program takes an imput from a player and compares it to an rng value to play a lottery game

import random

#initializing continue_game

guess = 1

while guess != -999 :
#the start game, here I am defining my variables and getting player input
    lot = random.randint(10,99)
    guess = int(input("\nEnter your lottery pick ( 2 digits) or -999 to quit: "))
    guess_digit1 = guess//10
    guess_digit2 = guess%10
    lot_digit1 = lot//10
    lot_digit2 = lot%10
#this is the main body of the game
    if guess == lot:
        print("Exact match: You win $10,000!")
    elif (guess_digit1 == lot_digit1 or guess_digit1 == lot_digit2) and (guess_digit2 == lot_digit1 or guess_digit2 == guess_digit2):
        print("Match all digits : You win $3,000")
    elif guess_digit1 == lot_digit1 or guess_digit1 == lot_digit2:
        print("Match one digit: You win $1,000")
    elif guess_digit2 == lot_digit1 or guess_digit2 == lot_digit2:
        print("Match one digit: You win $1,000")
    elif guess == -999:
        print("")
    else:
        print("Sorry no match")


#testrun 1
        
#Enter your lottery pick ( 2 digits) or -999 to quit: 44 
#Sorry no match 
 
#Enter your lottery pick ( 2 digits) or -999 to quit: 23 
#Match one digit:  You win $1,000 
 
#Enter your lottery pick ( 2 digits) or -999 to quit: 68 
#Match one digit:  You win $1,000 
 
#Enter your lottery pick ( 2 digits) or -999 to quit: 12 
#Match all digits :  You win $3,000 
 
#Enter your lottery pick ( 2 digits) or -999 to quit: 45 
#Exact match:  You win $10,000! 
 
#Enter your lottery pick ( 2 digits) or -999 to quit: -999
        
#testrun 2

#Enter your lottery pick ( 2 digits) or -999 to quit: 40
#Sorry no match

#Enter your lottery pick ( 2 digits) or -999 to quit: 55
#Sorry no match

#Enter your lottery pick ( 2 digits) or -999 to quit: 69
#Match one digit: You win $1,000

#Enter your lottery pick ( 2 digits) or -999 to quit: 34
#Match one digit: You win $1,000

#Enter your lottery pick ( 2 digits) or -999 to quit: 94
#Sorry no match

#Enter your lottery pick ( 2 digits) or -999 to quit: -999

#test run 3

#Enter your lottery pick ( 2 digits) or -999 to quit: 13
#Match all digits : You win $3,000

#Enter your lottery pick ( 2 digits) or -999 to quit: 13
#Match all digits : You win $3,000

#Enter your lottery pick ( 2 digits) or -999 to quit: 14
#Match all digits : You win $3,000

#Enter your lottery pick ( 2 digits) or -999 to quit: 53
#Sorry no match

#Enter your lottery pick ( 2 digits) or -999 to quit: 14
#Sorry no match

#Enter your lottery pick ( 2 digits) or -999 to quit: -999

# test run 4
#Enter your lottery pick ( 2 digits) or -999 to quit: 23
#Sorry no match

#Enter your lottery pick ( 2 digits) or -999 to quit: 93
#Sorry no match

#Enter your lottery pick ( 2 digits) or -999 to quit: 85
#Match all digits : You win $3,000

#Enter your lottery pick ( 2 digits) or -999 to quit: 28
#Sorry no match

#Enter your lottery pick ( 2 digits) or -999 to quit: 59
#Sorry no match

#Enter your lottery pick ( 2 digits) or -999 to quit: -999

#test run 5

#Enter your lottery pick ( 2 digits) or -999 to quit: 82
#Match one digit: You win $1,000

#Enter your lottery pick ( 2 digits) or -999 to quit: 74
#Sorry no match

#Enter your lottery pick ( 2 digits) or -999 to quit: 71
#Match one digit: You win $1,000

#Enter your lottery pick ( 2 digits) or -999 to quit: 46
#Match one digit: You win $1,000

#Enter your lottery pick ( 2 digits) or -999 to quit: 16
#Match one digit: You win $1,000

#Enter your lottery pick ( 2 digits) or -999 to quit: -999





    
        


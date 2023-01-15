#!/usr/bin/python3
import random

#for system to choose it's option through random selection
available_input_choices = ["rock", "paper", "scissors"]

#Loop to allow selecting either 3 or 5 rounds game to determine wining party
while True:
    #try close to check input and break or continue based on input check true or false 
    try:
        shots = int(input("Please select three or five rounds game by entering 3 or 5): "))
        if shots == 3 or shots == 5:
            break
        continue
    #Exception handling and letting user know input was not valid
    except ValueError:
        print("You entered Invalid Input")

#Determine win out of Odd number of iterations by dividing it by 2 and adding 1
winning_requires = int (shots/2)+1

#Winning count variables for both user and system
You_won = 0
System_won = 0
#put the code inside while loop to let user play multiple time without brecking out.
while True:
    while True:
        #promt user for input and save to variable for later use to determine result
        user_input = input ("Please enter one option from [rock, paper, scissors] : ")
        if user_input in available_input_choices:
            break
    #system select input randomly using random.choice()        
    system_input = random.choice(available_input_choices)

    #Display selections from both User and System
    print(" You selected ", user_input, "The system selected ", system_input, "\n")

    #Using conditional statements to compare and determine winner based on input values
    if user_input == system_input:
        print ("You and System both selected " , user_input , ".It is a Tie")
    elif user_input == "rock" and system_input == "paper":
        print ("Paper cover Rock! System Wins!")
        System_won += 1
    elif user_input == "rock" and system_input == "scissors":
        print ("Rock crushes scissors! You win!")
        You_won +=1
    elif user_input == "paper" and system_input == "rock":
        print ("Paper covers rock! You win!")
        You_won +=1
    elif user_input == "paper" and system_input == "scissors":
        print ("Scissors cut Paper! System wins!")
        System_won +=1
    elif user_input == "scissors" and system_input == "rock":
        print ("Rock crushes scissors! System win!")
        System_won +=1
    elif user_input == "scissors" and system_input == "paper":
        print ("Scissors cut Paper! You win!")
        You_won +=1
    if You_won == winning_requires or System_won == winning_requires:
        break
if You_won > System_won:
    print ("You win the Game!")
else:
    print ("System Wins this Time!")


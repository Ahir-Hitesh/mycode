#!/usr/bin/env python3
#Guessing game while loop practice

# round initialization at 0
round = 0

#while loop without loop ending condition
while True:
    #add 1 to screase round value at each iteration
    round = round + 1
    
    print('Finish the movie title, "Monty Python\'s The Life of ______"')
    #user input prompt
    answer = input("Your guess--> ")

    #condition to check if answer matches with correct answer
    if answer == 'Brian':
        print('Correct')
        #exit while loop if this if block was correct
        break
    #checking if round reached to 3 
    elif round==3:
        #print this message when round is 3 and answer did not match
        print("Sorry, the answer was Brian.")
        #Break out of loop if this block was executed 
        break
    #this block reached only if round not equal 3 and answer does not math to correct one
    else:
        print("Sorry! Try again!")


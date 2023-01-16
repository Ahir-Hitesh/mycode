#!/usr/bin/env python3
"""Amazon SDE Apprentice | Ahir-Hitesh"""

def main():
    while True:
        try:
            user_input = int (input("\nEnter number (1-100) of beer bottles to count down from! :"))
        except ValueError:
            print("Invalid entry! Please enter valid input.")
        else:
            if user_input > 100 or user_input < 1:
                print("Please keep number in between 1 and 100")
                continue
            else:
                for i in reversed(range(user_input)):
                    beerBottles = i + 1
                    print (f"{beerBottles} bottles of beer on the wall!")
                    print (f"{beerBottles} bottles of beer on the wall! {beerBottles} bottles of beer! You take one down, pass it arround!\n")
            break

if __name__ == "__main__":
    main()

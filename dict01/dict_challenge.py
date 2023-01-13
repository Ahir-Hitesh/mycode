#!/usr/bin/env python3
"""Understanding dictionaries
   {key: value, key:value, ...}
   using the del keyword with a dict
   adding and removing values from the dict"""

def main():
  
    #Save a user's input to the variable char_name from the following question:
    char_name = input (" Which character do you want to know about? (Starlord, Mystique, Hulk)\n")
    #capitalized appropriately (e.g. Peter Quill, not peter quill)
    char_name = char_name.title()
    #Save a user's input to the variable char_stat from the following question:
    char_stat = input (" What statistic do you want to know about? (real name, powers, archenemy)\n")
    #Make your script work no matter what capitalization the user provides!
    char_stat = char_stat.lower()

    ## create a dictionary with key:value pairs
    marvelchars= {
    "Starlord":
        {"real name": "peter quill",
        "powers": "dance moves",
        "archenemy": "Thanos"},

    "Mystique":
        {"real name": "raven darkholme",
        "powers": "shape shifter",
        "archenemy": "Professor X"},

    "Hulk":
        {"real name": "bruce banner",
        "powers": "super strength",
        "archenemy": "adrenaline"}
             }

    #Use the char_name and char_stat variables to pull value from the dictionary marvelchars
    print(char_name + "'s", char_stat, "is:", marvelchars.get(char_name).get(char_stat)) 

# call our main function
if __name__ == "__main__":
    main()

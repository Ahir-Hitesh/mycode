#!/usr/bin/env python3

#new list containing three season of year
season_list = ["spring", "summer", "winter"]

#add fourth season at the end of the list
season_list.append("fall") # this line will add "fall" to the end of our list

#prints list with added season 'fall' at the end of list
print(season_list)

#first remove fall from the list as it is added at wrong position in order of seasons
#remove() method will remove item matching passed parameter
season_list.remove("fall")

#since fall comes before winter in true order use insert to add it at correct position
season_list.insert(2, "fall")
print(season_list)

#!/usr/bin/python3
"""mplement search using sorted property of a list. The primary use
   case for this program is to search through data list to find the 
   target in minimal amount of time using divede and concour stretegy.
   Utilizing sort property we can make search more efficient compared 
   to going through each element of the list"""

# simple or brute force way of getting it done is to go through entire list 
# element at a time which takes operations n times where n is total elements
# Another way is to use the fact that in ordered list target could be either 
# on the left side or right side if we devide list at each iteration and cut 
# the input in half every time till target is found which is called binary dsearch.
def simpleSearch (myList, myTarget):


    for i in range(len(myList)):
        if myList[i] == myTarget:
            return i
    return -1
#myList = [ 8, 11, 26, 29, 31, 36, 49, 60, 77, 93]
if __name__ == '__main__':
    myTarget = 1
    myList = [1, 2, 5, 6, 9]
    print (simpleSearch(myList, myTarget))

'''while True:
    try:
        print("Enter a file name: ")
        name = input()
        with open(name, "w") as myfile:
            myfile.write("No problems with that file name.")
        break
    except:
        print("Error with that file name! Try again...")
'''

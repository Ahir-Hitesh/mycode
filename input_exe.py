#!/usr/bin/env python3

#List Challenge
#List one - wordbank 
wordbank= ["indentation", "spaces"] 

#List two - tlg sutdent names
tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu',
              'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed',
              'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 
              'Xiuxiang', 'Yaping']

#Append 4 to list one
wordbank.append(4)

#ask user for an input between 0 and 20. Save input value in variable num
num = int (input ("please enter number between 0 and 20: "))

#Base on input value asigned to num, name assigned to student_name from tlgstudent list
student_name = tlgstudents[num]

print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent.")


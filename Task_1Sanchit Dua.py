# [SIG Python Task 1] 

"""
#Tasks to performs: 
#a) Print 'Hello, World! From SIG Python - <your name>' to the screen
#b) Calculate Volume of a Sphere
#c) Create a customised email template for all students, 
   informing them about a workshop.

#PS: This is called a docstring... and it will not be interepreted
    So leave these instructions here.. no problems.
    The first line having '#' is called a comment. It will be ignored too.
    You can write your own comments and docstrings to make your code clear
    and documented.
#"""


# a) Print 'Hello, World! From SIG Python - <your name>' to the screen
# Write you code here
print("Hello, world! From SIG Python - <Sanchit Dua>")
print('')
print('')
print('')
print('')

# b) Calculate Volume of a Sphere
# Take the radius as input from the user and use the math module
import math
Radius = int(input("Enter the Radius of Sphere : "))
Volume = 4/3*math.pi*Radius**3
print('Volume of sphere is :  ', Volume )
print('')
print('')
print('')
print('')


#c) Create a customised email template for all students, informing them about a workshop that the student applied for earlier.
# Take the student's name, workshop, Time, Date, writer's name, organization's name 
# as input from the program's user 


# Use the given string as your template [This is a multi-line string]
student_name = input('Enter the name of student : ')
workshop = input('Enter the name of workshop : ')
Time = input('Enter the Time at which workshop is scheduled in HH : MM : ')
Date = input('Enter Date (in DD-MM-YYYY) : ')
writer_name = input('Enter writer name : ')
organization_name = input('Enter organisation name : ')
print('')
print('')
email_msg = print(f'''Dear {student_name},
We have received your request to register for the Workshop event and the 
workshop you applied for {workshop} has been scheduled at {Time}
on {Date}.

We will be seeing you there! Thanks for participating.

Regards,
{writer_name}
{organization_name}
''')
print(email_msg)


# NOTE: Make sure to print few empty lines after each task

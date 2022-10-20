# [SIG Python Task 2] 

"""
TODO: 
a) Write a program to solve a quadratic equation
b) Write the lyrics for '99 bottles of beer' using for loop
c) Solve Fizz Buzz using while loop.

NOTE: Have Fun Coding!
"""


# a) Write a program to solve a quadratic equation
"""
A quadratic equation is of the form ax^2 + bx + c
Take a, b, and c as float inputs from the user
Then calculate the roots of the equation using the determinant [b^2 - 4ac]
Note: import math module for mathematical operations like math.sqrt
"""
# Write you code here
import math
def quadraticroots(a, b, c):

    d = b * b - 4 * a * c
    sqr_val = math.sqrt(abs(d))


    if d > 0:
        print(" real and different roots ")
        print((-b + sqr_val) / (2 * a))
        print((-b - sqr_val) / (2 * a))

    elif d == 0:
        print(" real and same roots")
        print(-b / (2 * a))


    else:
        print("Complex Roots")
        print(- b / (2 * a), " + i", sqr_val)
        print(- b / (2 * a), " - i", sqr_val)
a = int(input("enter coefficient of a "))
b = int(input("enter coefficient of b"))
c = int(input("enter coefficient of c "))
if a == 0:
    print("Input right quadratic equation")

else:
    quadraticroots(a, b, c)
print("")
print("")
print("")
print("")
print("Question 2")
print("")
print("")
print("")
print("")

# b) Write the lyrics for '99 bottles of beer' using for loop
"""
There is a song called '99 bottles of beer'.
Its lyrices are provided here: http://www.99-bottles-of-beer.net/lyrics.html

You will notice that you can easily generate the lyrics for the song
if you use for loops for printing the lyrics in very few lines.
Your task is to print the lyrics for this song, using for loop.
"""
# Write you code here
#bottles = 99
#i=99
#for i in  bottles :
     #print(str(bottles) + " bottles of beer on the wall")
    # print(str(bottles) + " bottles of beer...")
     #print("take one down, pass it around")
     #print(str(bottles - 1) + " bottles of beer on the wall")
    # i = i - 1


# c) Solve Fizz Buzz using while loop.
"""
This is a very common and easy problem asked in job interviews.
The problem is as follows:
    Print integers 1 to N, but print “Fizz” if an integer is divisible by 3, “Buzz” if an integer is divisible by 5, and “FizzBuzz” if an integer is divisible by both 3 and 5.

    input: 15
    output: 
            1
            2
            Fizz
            4
            Buzz
            Fizz
            7
            8
            Fizz
            Buzz
            11
            Fizz
            13
            14 
            FizzBuzz

Use while loop to loop through number 1 to N, (take N as input from the user)
Use if, elif and else to check for given conditions.
"""
# Write your code here
a=1
b=int(input("Enter the value for N "))
i=0
while i in range(a,b):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
        continue
    elif i % 3 == 0:
        print("fizz")
        continue
    elif i % 5 == 0:
        print("buzz")
        continue
        i+=1
    print(i)

# NOTE: Make sure to print few empty lines after each task
# [SIG Python Task 3] 

"""
TODO: 
a) Calculate the temperature altitude from a list of temperatures
b) Count frequency of every character in a string (using dictionaries)
c) Verify De Morgan Laws (using sets)

NOTE: Have Fun Coding!
"""


# a) Calculate the temperature altitude from a list of temperatures
"""
Given a list of temperatures of one day, calculate the temperature amplitude (difference between highest and lowest temperature). Keep in mind that sometimes there might be a sensor error (represented as 'error').
"""

#temperatures = [3, -20, -6, -12, 'error', 24, 18, 28, 16, 14]

# Write you code here
def temperature():
  m=a=0
  temp = [3, -20, -6, -12, 'error', 24, 18, 28, 16, 14]
  for i in temp:
    if type(i) is int:
       if a<i:
          a=i
       if m>i:
          m=i
  diff=a-m
  print("TEMPERATURE ALLTITUDE IS =")
  print(diff)



print("")
print("")




# b) Count frequency of every character in a string (using dictionaries)
"""
Take a string as input from the user (for eg: 'abcccedeEEdffaG') and count the frequency each characters occurs in the string.

NOTE: Covert the string to upper or lower case first.
"""
# Write you code here
def sec():
    istr=input("enter the string ")
    freq = {}
    print(istr.upper())
    for char in istr:
        if char in freq:
          freq[char] += 1
        else:
         freq[char] = 1
    print("Per char frequency in '{}' is :\n {}".format(istr, str(freq)))
print("")
print("")



# c) Verify De Morgan Laws (using sets)
"""
Given a Universal Set 'U', and two of its subsets 'A' and 'B'
Verify the De Morgan laws using sets. 

# De Morgan Laws:
not (A or B) = not A and not B
not (A and B) = not A or not B

NOTE: Use the inbuilt operators/methods for set operations (intersection, union, difference, ...)
NOTE: Complement of a set 'X' is the difference: 'U' - 'X'
"""

U = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
A = {0, 2, 4, 6, 8}
B = {3, 6, 9}

# Write your code here
def morgan():
    U = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    A = {0, 2, 4, 6, 8}
    B = {3, 6, 9}
    x = (not(A and B))==((not A) or (not B))
    y = (not(A or B))==((not A) and (not B))
    print('x is :', x, '\n y is :' ,y)
    print("Hence De Morgan's Law is Verified")



# NOTE: Make sure to print few empty lines after each task
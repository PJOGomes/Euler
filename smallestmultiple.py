"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import math

def greatestDivider(number):
    greatest_divider=1
    for i in range (1, number):
        if (number %i == 0):
            greatest_divider=i
    return greatest_divider

number = int(input("Enter the number"))
mult = []

for i in range (2, number+1):
    divider = greatestDivider(i)
    if(divider ==1):
        mult.append(i)
start = 1
for i in mult:
    start *=i
print("Begin at", start)
print("Stop at", math.factorial(number))
for i in range (start, math.factorial(number)):
    count = 0
    for j in range (2, number+1):
        if(i%j==0):
            count +=1
        else:
            break
    if(count == number-1):
         print("The smallest number is ", i)
         break
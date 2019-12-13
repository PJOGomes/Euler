"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
number = int(input("Enter the number:"))

#Function to return greatest divider of a number
def greatestDivider(number):
    greatest_divider=1
    for i in range (1, number):
        if (number %i == 0):
            greatest_divider=i
    return greatest_divider

#Check the divider of a given number
for i in range(1, number+1):
    prime = 1
    if(number % i ==0):
        print("{} divides {}".format(i, number))
        prime = greatestDivider(i)
        if(prime==1):
            print("{} is a prime divider of {}".format(i, number))


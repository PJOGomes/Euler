"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""
number=int(input("Enter the number of primes you want: "))

def greatestDivider(number):
    greatest_divider=1
    for i in range (1, number):
        if (number %i == 0):
            greatest_divider=i
    return greatest_divider

primes = []
start = 2
while True:
    divider = greatestDivider(start)
    if(divider == 1):
        primes.append(start)
    if(len(primes)==10001):
        break
    else:
        print(len(primes))
        start +=1
print(primes[10000])
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""
import math
number = int(input("Insert max value: "))

def checkPrime(number):
    div =[]
    value = int(math.sqrt(number))

    for i in range(2, value+1):
        if(number % i ==0):
            return False
    return True

sum =0
for i in range(2, number):
    value = checkPrime(i)

    if(value == True):
        sum+=i
        print("{}==>{}".format(i, sum))

print("Soma final: ", sum)
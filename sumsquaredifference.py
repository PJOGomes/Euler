"""
The sum of the squares of the first ten natural numbers is,
1² + 2² + ... + 10² = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)² = 55² = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
import math

number = int(input("Enter the number: "))

# The sum of the first n numbers starting with 1 is (n+1)*n/2
number_sum = int((number + 1) * number / 2)
print("The sum of the numbers until {} is {} and it's square is {}".format(number, number_sum,
                                                                           int(math.pow(number_sum, 2))))

# The sum of the first n square numbers starting with one is n(n+1)(2n+1)/6
square_number_sum = int((number * (number + 1) * (2 * number + 1)) / 6)
print("The sum of the square of the {} numbers is {}".format(number, square_number_sum))

print("The difference is ", (int(math.pow(number_sum, 2)) - square_number_sum))

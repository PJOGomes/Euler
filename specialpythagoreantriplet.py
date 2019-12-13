"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a² + b² = c²
For example, 3² + 4² = 9 + 16 = 25 = 52.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

for a in range(1, 1000):
    for b in range(a, 1000 - a):
        c = 1000 - a - b
        if (a * a + b * b == c * c):
            print(a, b, c)
            print("Product: {}".format(a * b * c))

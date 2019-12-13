"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
"""
#We know we only move to the right and down, and that we have the sam amount of moves to the right and down
#We want to go from (0,0) to (20,20) in terms of coordinates

import math
print(int(math.factorial(40)/(math.pow(math.factorial(20),2))))
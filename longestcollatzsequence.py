"""
The following iterative sequence is defined for the set of positive integers:
n → n/2 (n is even)
n → 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.
"""
max =0
index =0
number = int(input("Enter top value: "))
#print("{}->".format(number))
for i in range(2, number+1):
   # print("Checking the chain starting at ", i)
    value = i
    chain = 0
    while (value!=1):
        if(value %2==0):
            value = int(value/2)
            chain +=1
           # print("{}->".format(value))
        else:
            value = 3* value +1
            chain += 1
            #print("{}->".format(value))
    print("Chain size for {} is {}".format(i, chain))
    if(chain>max):
        max=chain
        index = i
print("Max chain size {} for number {}".format(max, index))
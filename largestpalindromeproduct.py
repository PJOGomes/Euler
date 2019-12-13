"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
#Check if a number is a palindrome
def checkPalindrome(number):
    temp = str(number)
    #We know that the string temp has 5 or 6 characters
    if(number>99999):
        if (temp[0]==temp[5] and temp[1]==temp[4] and temp[2]==temp[3]):
            return True
        else:
            return False
    else:
        if (temp[0]==temp[4] and temp[1]==temp[3]):
            return True
        else:
            return False
#Get all the multiplications of 3-digit number
palindrome = []
for i in range (100, 1000):
    for j in range (100, 1000):
        value = False
        mult = i*j
        if(checkPalindrome(mult)):
            #Add to the palindrome list
            palindrome.append(mult)

#Sort the palindrome list from highest to lowest
palindrome.sort(reverse=True)
#Get the highest palindrome
print("{} is the highest palindrome".format(palindrome[0]))
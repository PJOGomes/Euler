prev_term =1
term=2
sum = 2
while (term<4000000):
    temp = prev_term
    prev_term=term
    term +=temp
    if(term%2==0):
        sum+=term
print(sum)
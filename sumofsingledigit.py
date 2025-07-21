#sum of digitsof a random number
#until it gets single digit

import random
n=int(input('enter a number:'))
while True:
    s=0    
    while n>0:
           digit=n%10
           s+=digit
           n//=10
    if s>9:
       n=s
    else:
       print(s)
       break


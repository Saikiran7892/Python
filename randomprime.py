#Write a Python program to generate a random number between 1 and 100
#check whether it is prime or not

import random

random_number=random.randint(1,100)
print(random_number)
i=1
d=2
while i<=random_number//2:
    if random_number%2==0:
        print('is not prime')
        break
    i+=1
else:
    print('is prime')
 
    

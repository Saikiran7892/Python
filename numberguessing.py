
import random
random_number=random.randint(1,40)
is_true=True
while is_true:
     num=int(input('guess a number:'))
     if num==random_number:
        print('its correct')
        is_true=False
     elif num>random_number:
        print('too high')
     else:
        print('its low ')
     
print('end of the program')
 
        

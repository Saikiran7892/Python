#prime number

num=int(input('enter a number:'))
count=0
i=1
while num%i==0:
    count+=1
    i+=1
    if count>2:
        print('is not prime')

    else:
        print('is prime')
    

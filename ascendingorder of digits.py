#ascending order of digits


num=int(input('enter a number:'))
bkp=num
i=0
while i<=9:
    temp=bkp
    while temp!=0:
        digit=temp%10
        if digit==i:
            print(i,end='')
        temp//=10
    i+=1

    
 
    

#descending order


num=int(input('enter a number:'))
bkp=num
i=9
while i>=0:
    temp=bkp
    while temp!=0:
        digit=temp%10
        if digit==i:
            print(i,end='')
        temp//=10
    i-=1

    
 
    

#prime numbers b/w 1 to 50

i=1
 
while i<=50:
    d=0
    num=1
    while num<=i:
        if i%num==0:
            d+=1
        num+=1 
    if d==2:
       print(i,'is a prime')       
    i+=1
    

 
        

#sum of even numbers in fibnocci series
n=int(input('enter a number:'))
a=0
b=1
i=1
s=0
while i<=n:
    c=a+b
    if c%2==0:
        s=s+c
        print(s)
    a=b
    b=c
    i+=1

    

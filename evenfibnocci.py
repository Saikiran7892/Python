#even fibnocci numbers

n=int(input('enter a number:'))
a=0
b=1
i=1
while i<=n:
    c=a+b
    if c%2==0:
        print(c,'even fibnocci number')
    a=b
    b=c
    i+=1

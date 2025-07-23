#fibnocci number or not
n=int(input('enter a number:'))
a=0
b=1
while True:
    c=a+b
    if c==n:
        print(c,'is fibnocci number')
        break
    if c>n:
        print(c,'is not fibnocci number')
        break
    a=b
    b=c
        

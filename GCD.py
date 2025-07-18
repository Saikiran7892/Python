#GCD of two numbers

n1=int(input('enter a number:'))
n2=int(input('enter a number:'))
if n1<n2:
    small=n1
else:
    small=n2

d=small
while d>=2:
    if n1%d==0 and n2%d==0:
        print('GCD is',d)
        break
    small-=1
else:
    print('no GCD')

#perfect number

n=int(input('enter a number:'))
i=1
s=0
while i<=n//2:
    if n%i==0:
        s=s+i
    i+=1

if s==n:
    print('perfect number')
else:
    print('not perfect number')
    

#perfect number or not
#if perfect number check even or not

n=int(input('enter a number:'))
i=1
s=0
while i<=n//2:
    if n%i==0:
        s+=i
    i+=1

if s==n:
    if n%2==0:
        print('perfect number and even')
    else:
        print('perfect number but not even')
else:
    print('not perfect number')
    


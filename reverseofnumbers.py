#reverse from n to 1

n=int(input('enter nth number:'))

while n>=1:
    rev=n%10
    print(rev)
    n-=1

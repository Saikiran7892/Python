#count of even numbers

n=int(input('enter a number:'))
c=0
while n!=0:
    digit=n%10
    if n%2==0:
        c+=1
    n//=10
print(c)

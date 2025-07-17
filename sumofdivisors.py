#sum of divisors of given number

num=int(input('enter a number:'))
s=0
i=1
while i<=num:
    if num%i==0:
        s=s+i
    i+=1
print(s)

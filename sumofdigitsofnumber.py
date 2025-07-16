#sum of digits of a number
num=int(input('enter a number:'))
s=0
while num!=0:
    digit=num%10
    s=s+digit
    num=num//10
print(s)

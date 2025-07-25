#sum of factorial of digit in a number

num=int(input('enter a number:'))
original=num
s=0
while num!=0:
    digit=num%10
    f=1
    while digit>0:
        f=f*digit
        digit-=1
    s+=f
    num//=10
if s==original:
   print('given number is a strong number')
else:
   print('given number is not a strong number')

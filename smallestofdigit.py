#smallest digit of a number

num=int(input('enter a number:'))
temp=0
digit=0
while num!=0:
    temp=digit
    digit=num%10
    if digit<=temp:
       print(digit)
    
    num=num//10

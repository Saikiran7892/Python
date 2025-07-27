#smallest digit in a number

 
num=int(input('enter a number:'))
temp=1
while num!=0:
    digit=num%10
    if digit<=temp:
       temp=digit
    num=num//10

print(temp)

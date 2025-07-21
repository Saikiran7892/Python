#biggest digit

num=int(input('enter a number:'))
big=0
while num>0:
    digit=num%10
    if big<digit:
        big=digit
    num=num//10
print(big)

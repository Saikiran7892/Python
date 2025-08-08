#second largest digit

num=int(input('enter a number:'))
first=0
second=0

while num!=0:
    digit=num%10
    if digit>first:
        second=first
        first=digit
    if digit>second and digit<first:
        second=digit
    num//=10
print(second)

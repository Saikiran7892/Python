#factorial of a number

num=int(input('enter a number:'))
f=1
while num>0:
    f=f*num
    num-=1
print(f)

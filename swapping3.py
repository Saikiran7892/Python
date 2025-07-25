#swapping without using another variable

n1=int(input('enter a number:'))
n2=int(input('enter a number:'))

n1=n1+n2
n2=n1-n2
n1=n1-n2
print('n1=',n1)
print('n2=',n2)

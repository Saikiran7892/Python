#fibonacci number

a=0
b=1
print(a,b,end=' ')
for i in range(1,11):
    c=a+b
    print(c,end=' ')
    a=b
    b=c
 

#Write a Python program to input two integers and perform the following:
##If both numbers are even, print their sum.
#If both numbers are odd, print their product.
#If one is even and the other is odd, print the difference (first - second)

n1=int(input('enter a number:'))
n2=int(input('enter a number:'))

while True:
    if n1%2==0 and n2%2==0:
        s=n1+n2
        print(s)
        break
    elif n1%2==1 and n2%2==1:
        product=n1*n2
        print(product)
        break
    else:
        diff=n1-n2
        print(diff)
        break


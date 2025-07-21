#Write a Python program to determine if a given number num is even or odd.
#If it's even, check if it's greater than 10 and print appropriate messages.

num=int(input('enter a number:'))
while num%2==0:
    print('even')
    if num>10:
        print(num,'is even number and greater than 10')
        break
else:
    print('odd')

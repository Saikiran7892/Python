#finding largest of four numbers

num1=int(input('enter number1:'))
num2=int(input('enter number2:'))
num3=int(input('enter number3:'))
num4=int(input('enter number4:'))

if num1>num2 and num1>num3 and num1>num4:
    print('largest number is:',num1)
elif num2>num1 and num2>num3 and num2>num4:
    print('largest number is:',num2)
elif num3>num1 and num3>num2 and num3>num4:
    print('largest number is:',num3)
else:
    print('largest number is:',num4)

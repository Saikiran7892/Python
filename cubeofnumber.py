number=int(input('enter number:'))
cube=round(number**(1/3))
if cube**3 == number:
    print('cube of number is:',cube)
else:
    print("not perfect cube")
print('end of program')

#LCD
'''
step1:read the two numbers
step2:find the smallest number
step3:find the common divisors
step4:show the output'''

n1=int(input('enter a number:'))
n2=int(input('enter a number:'))
if n1<n2:
    small=n1
else:
    small=n2
i=2
while i<=small:
    if n1%i==0 and n2%i==0:
        print('LCD',i)
        break
    i+=1
else:
    print('no LCD')

#checking given number existing in a list

x=[3,4,6,2,8]

user_input=int(input('enter a number:'))

for i in x:
    if i == user_input:
        print('Yes')
        break
else:
    print('No')

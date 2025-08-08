
#Rotation of lists

x=[1,2,3,4,5,6]

rotation=input('enter rotation(LR/RR):')

n=int(input('enter number of elements to rotate:'))

num=n%len(x)

for i in x:
    if rotation=='RR':
        print(x[-num:]+x[:-num])
        break
    elif rotation=='LR':
        print(x[num:]+x[:num])
        break
    else:
        print('choose correct option')
        break
    
        

#missing number in list

list=[1,2,3,5]
n=5


for j in range(1,n+1):
    if j not in list:
        print(j,'is missing number')
        break
else:
    print('not have missing number')
    

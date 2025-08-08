

list=[2,3,4,50,60,20,35]

num=int(input('enter a element number:'))

for i in list:
    if i==num:
        inx=list.index(i)
        break
print(inx,'is the index of ',num)
    
     
    

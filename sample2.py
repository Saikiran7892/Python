

x=[1,3,2,4,1,2,3,4,5,2,6,3,2,3,2,3,4,7]

element=int(input('enter a element:'))
cnt=0
for i in range(0,len(x)):
    
    if x[i]==element:
        cnt+=1
        if cnt==2:
            print(i)
             
 
 

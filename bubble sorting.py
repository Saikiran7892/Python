

x=[10,5,15,16,3,2,4]

for j in range(0,len(x)-1):
    for i in range(0,len(x)-j-1):
        if x[i]>x[i+1]:
           x[i],x[i+1]=x[i+1],x[i]
     
    
 

print(x)

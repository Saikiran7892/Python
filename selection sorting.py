#selection sort


x=[10,6,2,3,4,7,1,8,9,5,2,4,5,3]

for i in range(0,len(x)):
    min_value=min(x[i:])
    idx=x[i:].index(min_value)+i
    x[i],x[idx]=x[idx],x[i]
    
print(x)
 

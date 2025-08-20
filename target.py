



def istarget(x,target):
    output=[]
    for i in range(0,len(x)):
        for j in range(i+1,len(x)):
            if x[i]+x[j]==target:
                pair=sorted((x[i],x[j]))
                if pair not in output:
                    output+=[pair]
                
                
    return output

list=[1, 3, 2, 2, 4, 5]
res=istarget(list,5)
print(res)
        
        
    

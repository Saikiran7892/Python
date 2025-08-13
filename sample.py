x=[1,3,2,4,2,1,2,1,2]

output=[]

for i in x:
    cnt=0
    for j in x:
        if i==j:
            cnt+=1
    if cnt>1:
        if i not in output:
           output+=[i]

print(output)
    
            
            

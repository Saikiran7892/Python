


x=[3,0,2,0,1,0,4,0,51,2]

def isfine(list):
    for i in range(len(list)):
        if list[i]==0:
            for j in range(i+1,len(list)):
                if list[j]!=0:
                    list[i],list[j]=list[j],list[i]
                    break
                
                 
    return list
res=isfine(x)
print(res)

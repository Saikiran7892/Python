



   

def isfine(num):
    a=[]
    cnt=0
    for i in num:
        cnt=0
        for j in num:
            if i==j:
                cnt+=1
    
        if cnt==1:
            a.append(i)
    return a



list=[1, 2, 2, 3, 4, 4, 5]
res=isfine(list)
print(res)



 

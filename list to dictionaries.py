


x1=['a','b','c']
x2=[1,2,3]


def isfine(x,y):
    d={}
    for i in range(0,len(x)):
        d[x[i]]=y[i]
    return d

res=isfine(x1,x2)
print(res)
        

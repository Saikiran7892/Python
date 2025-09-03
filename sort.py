


d={'z':10,'k':15,'c':1,'a':2}

res=list(d.items())


for i in range(0,len(res)):
    for j in range(i+1,len(res)):
        if res[i][0]>res[j][0]:
            res[i],res[j]=res[j],res[i]

print(dict(res))

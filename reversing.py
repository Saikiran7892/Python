

d={'a':1,'b':2,'c':4}

def isfine(s):
    d1={}
    for i in s:
        if s[i] not in d1:
            d1[s[i]]=i
            
    return d1
res=isfine(d)
print(res)

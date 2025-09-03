

name=input('enter a name:')


def isfine(st):
    d={}
    for ch in st:
        cnt=st.count(ch)
        if ch not in d:
            d[ch]=cnt
    return d

res=isfine(name)
print(res)
        

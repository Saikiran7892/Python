



def isrepeating(s,e):
    cnt=0
    for i in range(s,e+1): 
        cnt+= str(i).count('2')   
    return cnt


res=isrepeating(1,100)
print(res)

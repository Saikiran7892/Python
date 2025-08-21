


s='Python'

def isreverse(st):
    output=''
    #for ch in range(len(st)-1,-1,-1):
        #output+=st[ch]
    for ch in st:
        output=ch+output
    return output
res=isreverse(s)
print(res)
        

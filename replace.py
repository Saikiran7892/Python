


s='we are learning python are are'
what='are'
whom='am'
occurrence=2
def isreplace(st):
    output=''
    if (what in st) and occurrence<=st.count(what):
        cnt=0
        for i in range(0,len(st)):
            if st[i:i+len(what)]== what:
                cnt+=1
                if cnt==occurrence:
                    output=st[:i]+whom+st[i+len(what):]
                
        return output
    else:
        return 'replace not possible'
    
res=isreplace(s)
print(res)

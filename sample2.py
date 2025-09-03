


s='aaabbcddd'

st=''

i=0
 

while i<len(s):
    cnt=1
    while i+1<len(s) and s[i]==s[i+1]:
        cnt+=1
        i+=1
    st+=s[i]+str(cnt)
    i+=1
print(st)
        
    

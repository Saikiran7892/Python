

s='Education is important'
def isvowels(st):
    cnt=0
    for ch in st:
        if ch in 'aeiouAEIOU':
            cnt+=1
    return cnt
res=isvowels(s)
print(res)



s='Programming is fun'

def isvowel(st):
    output=''
    for ch in st:
        if ch in 'aeiouAEIOU':
            output=output+ch
    return output

res=isvowel(s)
print(res)
            

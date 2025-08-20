

s='abc23j4'


def sumofdigit(st):
    s=0
    for ch in st:
        if ch in '0123456789':
            s=s+int(ch)
    return s

res=sumofdigit(s)
print(res)
            

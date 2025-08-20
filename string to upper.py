

 


def isstring(st):
    output=''
    for ch in st:
        a_code=ord(ch)
        if a_code>=97 and a_code<=122:
            output=output+chr(a_code-32)
        else:
            output=output+ch
    return output


s='we are good students'
res=isstring(s)
print(res)
        

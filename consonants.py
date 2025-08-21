

s='Python is cool'

def isconsonants(st):
    output=''
    for ch in st:
        if ch!=' ': 
           if ch not in 'aeiouAEIOU':
               output+=ch+' '
    return output

res=isconsonants(s)
print(f"'{res}'")
            

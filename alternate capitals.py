


s='we are good students'


def isfine(st):
    output=''
    for ch in range(0,len(st)):
        if ch%2==0:
            a=ord(st[ch])
            if a>=97 and a<=122:
                output+=chr(a-32)
            else:
               output+=st[ch]
        else:
             b=ord(st[ch])
             if b>=65 and b<=90:
                output+=chr(b+32)
             else:
                 output+=st[ch]
    return output


res=isfine(s)
print(res)
        
        
    
        
            
        

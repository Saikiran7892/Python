
s='we-are|good,students'

def isfine(st):
    delimiter=[',','|','-',';']
    word=''
    output=[]
    for ch in st:
        if ch in delimiter:
            output.append(word)
            word=''
        else:
            word=word+ch
    else:
       output.append(word)
    return output
        
res=isfine(s)
print(res)


#out=s.split('|')
#print(out)

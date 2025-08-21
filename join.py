

list=['python','is','cool']


def isjoin(num):
    output=''
    for i in range(0,len(num)):
        if i==len(num)-1:
            output+=num[i]
        else:
            output+=num[i]+'-'
    return output
res=isjoin(list)
print(res)
        
        



def isprimenumber(num):
    for d in range(2,(num//2)+1):
        if num%d==0:
            break
    else:
        return True
     

def isprime(num):
    a=[]
    for i in num:
        if isprimenumber(i)== True:
            a.append(i)
    return a
            
            
            
           

list=[2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
res=isprime(list)
print(res)
 

        
        

        

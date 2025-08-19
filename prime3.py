
def isprimenumber(num):
    for d in range(2,(num//2)+1):
        if num%d==0:
            break  
    else:
        return True


def isprime(s,e):
    for i in range(s,e+1):
        if isprimenumber(i):
            print(i)

res=isprime(1,100)




    
            

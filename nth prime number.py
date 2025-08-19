



def isprimenumber(num):
    if num<2:
        return False
    for d in range(2,(num//2)+1):
        if num%d==0:
            return False
    return True

    
def isprime(s):
    cnt=0
    n=int(input('enter a nth number:'))
    num=s
    while True:
        if isprimenumber(num):
            cnt+=1
            if cnt==n:
                return num
        num+=1

res=isprime(2)
print(res)
            
            

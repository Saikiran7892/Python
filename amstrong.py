

def isdigitcount(num):
    d_cnt=0
    while num>0:
        num=num//10
        d_cnt+=1
    return d_cnt


def sumofdigitpower(num,p):
    s=0
    while num>0:
        q=num%10
        s=s+q**p
        num=num//10
    return s

def isamstrong(num):
    cnt=isdigitcount(num)
    s=sumofdigitpower(num,cnt)
    
    if s == num:
        return True
    return False
  


res=isamstrong(153)
print(res)

 

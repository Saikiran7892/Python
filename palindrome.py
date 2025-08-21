

list=[121, 123, 454, 789, 989]

def isreverse(num):
    rev=0
    while num>0:
        rem=num%10
        rev=rev*10+rem
        num=num//10
    return rev
        

def ispalindrome(num):
    output=[]
    for i in num:
         
        if isreverse(i) == i:
            output+=[i]      
    return output
            

res=ispalindrome(list)
print(res)

 

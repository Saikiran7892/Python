#1-1000 strong numbers

i=1
while i<=1000:
    temp=i
    s=0
    while i!=0:
        j=i%10
        f=1
        while j!=0:
             f=f*j
             j-=1
        s+=f
        i//=10
    i=temp
    if s == i:
        print(i)
    i+=1
     

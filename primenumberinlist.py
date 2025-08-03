#prime number in list

x=[4,5,8,11,13,18,21,23]
prime=[]
for i in x:
    for j in range(2,i//2+1,1):
        if i%j==0:
            break
    else:
      prime.append(i)
        
print(prime)

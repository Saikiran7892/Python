#1-1000 perfect numbers


i=1
while i<=1000:
    j=1
    s=0
    while j<=i//2:
       if i%j==0:
         s=s+j
       j+=1
    if s==i:
      print(i)

    i+=1
   


    

    


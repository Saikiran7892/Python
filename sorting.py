


#x=[30, "py", 50, 80, 30, "jy", 20]
x=[30,'py',50,80,30,'jy',20]

for i in range(0,len(x)):
    if type(x[i])==int:
       for j in range(i+1,len(x)):
            if type(x[j])==int:
               if  x[i]>x[j]:
                   x[i],x[j]=x[j],x[i]
            else:
                continue
    else:
        continue
     
print(x)

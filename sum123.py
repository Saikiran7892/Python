#sum of numbers from 1 to 100
#skipping the numbers divisible by both 3 and 5

i=1
s=0
while i<=100:
    if i%3==0 and i%5==0:
       i+=1
       continue
    s+=i
    i+=1
     
print(s)

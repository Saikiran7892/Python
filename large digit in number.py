

num=int(input('enter a number:'))
temp=num
d_cnt=0
large=0
while num!=0:
    num//=10
    d_cnt+=1


num=temp
for i in range(1,d_cnt+1):
    while num!=0:
       digit=num%10
       if digit>large:
         large=digit
       num//=10
print(large)
    

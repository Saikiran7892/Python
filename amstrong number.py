#amstrong number


num=int(input('enter a number:'))
temp=num
d_cnt=0
while num!=0:
    num//=10
    d_cnt+=1

num=temp
s=0
while temp!=0:
    digit=temp%10
    s=s+(digit**d_cnt)
    temp//=10

if s==num:
    print('amstrong number')
else:
    print('not a amstrong number')
    

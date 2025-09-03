

d={10:'X',9:'IX',5:'V',4:'IV',1:'I'}

num=int(input('enter a number:'))
roman=''

for i in d:
    q=num//i
    if q>0:
        roman+=d[i]*q
    num%=i

print(roman)



roman=['C','XC','L','XL','X','IX','V','IV','I']

decimal=[100,90,50,40,10,9,5,4,1]

num=int(input('enter a number:'))

for d in decimal:
    q=num//d
    if q>0:
        indx= decimal.index(d)
        print(roman[indx]*q,end='')
        num%=d




#leap year using alternative method

year=int(input('enter year:'))
if year%4==0:#2020%4==0--T
    if year%100==0:#2020%100==0--F
        if year%400==0:
           print('leap year')
        else:
           print('not a leap year')
    else:
        print('leap year')
else:
    print('not a leap year')

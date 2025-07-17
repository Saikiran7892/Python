#leap year

year=int(input('enter a year:'))
while year:
    if year%4==0:
        if year%100==0:
            if year%400==0:
                print('leap year')
                break
            else:
                print('not a leap year')
                break
        else:
            print(' leap year')
            break
    else:
        print('not leap year')
        break
print('end of the program')

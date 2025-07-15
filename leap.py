#leap year


'''
step1: enter a year
step2: if year%4==0 -- true then year%100==0 -- false -->leap year
step3: if year%100==0 --true then year%400==0 --true -->leap year
step4: tell output'''

year = int(input('enter a year:'))

if (year%100==0 and year%400==0) or (year%4==0 or year%100==0):
#(2024%100==0 and 2024%400==0) or (2024%4==0 or 2024%100==0)
#(F and F) or (T or F)
#F or T-->T
    print('leap year')
    
else:
    print('not a leap year')


''' Write a Python program to check whether a password is strong or not.
 A strong password must:
Be at least 8 characters long
Contain at least one uppercase letter
Contain at least one lowercase letter
Contain at least one digit
Contain at least one special character (like @, #, $, etc.)
input:Vcube@123'''


password=input('enter a password:')

def isstrong(st):
    if len(st)>=8:
        has_upper=False
        has_lower=False
        has_digit=False
        has_symbols=False
        symbols=['@','#','$','^','&','*']
        for ch in st:
            if 'A'<=ch<='Z':
                has_upper=True
            elif 'a'<=ch<='z':
                has_lower=True
            elif ch in '0123456789':
                has_digit=True
            elif ch in symbols:
                has_symbols=True
        return has_upper and has_lower and has_digit and has_symbols
            
         
    else:
        return 'Invalid password'


if isstrong(password):
    print('Strong')
else:
    print('weak')


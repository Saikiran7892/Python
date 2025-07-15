#%2,%3,%7-python
#AI


num=int(input('enter number:'))#15
if (num%2==0) and (num%3==0 or num%7==0):#(15%2==0) and (15%3==0 or 15%7==0)  -->(F) and (T or F) --> F and T -->F
    print('PYTHON')
else:
    print('AI')

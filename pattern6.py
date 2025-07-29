rows=int(input('enter number of rows:'))
row_no=1

while row_no<=rows:
    print(' '*(rows-row_no),'*'*(2*row_no-1))
    row_no+=1

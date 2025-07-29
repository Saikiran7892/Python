#upside-down pyramid pattern

rows=int(input('enter number of rows:'))
row_no=1
while row_no<=rows:
    print(' '*(row_no-1),'*'*(2*rows-2*row_no+1))
    row_no+=1

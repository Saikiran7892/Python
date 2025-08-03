#diamond hallow pattern


rows=int(input('enter a number of rows:'))
middle_row=(rows//2)+1

for row_no in range(1,rows+1):
    if row_no==1 or row_no==rows:
        print(' '*(rows-middle_row),'*',sep='')
    elif row_no<=middle_row:
        print(' '*(middle_row-row_no),'*',' '*(2*row_no-3),'*',sep='')
    else:
        print(' '*(row_no-middle_row),'*',' '*(2*rows-2*row_no-1),'*',sep='')



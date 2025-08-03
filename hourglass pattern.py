#hourglass pattern

rows=int(input('enter a number of rows:'))
middle_row=(rows//2)+1
for row_no in range(1,rows+1):
    if row_no==1 or row_no==rows:
        print('*'*(rows))
    elif row_no<=middle_row:
        print(' '*(row_no-1),'*'*(2*middle_row-2*row_no+1),sep='')
    else:
        print(' '*(rows-row_no),'*'*(2*row_no-2*middle_row+1),sep='')
              


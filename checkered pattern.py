#checkered pattern


rows=int(input('enter a number of rows:'))
middle_row=(rows//2)+1
for row_no in range(1,rows+1):
    if row_no==1 or row_no==rows:
        print('*'*(rows+1))
    elif row_no<middle_row:
        print('*',' '*(2*row_no),'*',sep='')
    elif row_no==middle_row:
        print('*'*(row_no+1),' ','*',sep='')
    else:
        print('*',' '*(row_no-2),'*',' ','*',sep='')

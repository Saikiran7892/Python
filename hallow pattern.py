#hollow half pyramid pattern

rows=int(input('enter number of rows:'))
for row_no in range(1,rows+1):
    if row_no==1 or row_no==rows:
        print('*'*row_no)
    else:
        print('*',' '*(row_no-1),'*',sep='')
        



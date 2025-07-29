#right-aligned asterisks

rows=int(input('enter number of rows:'))

row_no=1

while row_no<=rows:
    print(' '*(rows-row_no),'*'*row_no)
    row_no+=1

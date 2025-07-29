#simple pattern of decreasing asterisks

rows=int(input('enter number of rows:'))

rows_no=1
while rows_no<=rows:
    print('*'*(rows-rows_no+1))
    rows_no+=1

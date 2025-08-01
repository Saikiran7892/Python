#alphabet pattern


rows=int(input('enter number of rows:'))

for row_no in range(1,rows+1):
    print(chr(64+row_no)*row_no,sep='')

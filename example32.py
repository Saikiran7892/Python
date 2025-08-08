


rows=int(input('enter a number of rows:'))


for row_no in range(1,rows+1):
    for i in range(row_no,row_no+1):
        print(chr(64+i)*row_no,end='')
    print()


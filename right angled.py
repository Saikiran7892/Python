#right-angled pattern


rows=int(input('enter a number of rows:'))

for row_no in range(1,rows+1):
    for _ in range(1,row_no+1):
        print(_,end='')
    print()

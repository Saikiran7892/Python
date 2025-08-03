#pattern of numbers in an inverted pyramid


rows=int(input('enter a number of rows:'))


for row_no in range(1,rows+1):
    for i in range(1,rows-row_no+2):
        print(i,end='')
    print()

# 1
# 2 4
# 4 6 8
# 7 9 11 13
#11 13 15 17 19


rows = int(input("Enter number of rows: "))

for row_no in range(1, rows + 1):
    for num in range(row_no,row_no+1):
        print(num, end=' ')
        num+=2
    print()   

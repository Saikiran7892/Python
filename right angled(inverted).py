#right-angled triangle(inverted)

rows=int(input('enter a number of rows:'))


for row_no in range(1,rows+1):
    for i in range(row_no,0,-1):
        print(i,end='')
    print()

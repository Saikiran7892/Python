#inverted right-angled

rows=int(input('enter a number of rows:'))

for row_no in range(rows,0,-1):
    for _ in range(1,row_no+1):
        print(_,end='')
    print()

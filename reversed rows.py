#right angled triangle witha reversed rows
rows=int(input('enter a number of rows:'))

for row_no in range(rows,0,-1):
    for i in range(row_no,0,-1):
        print(row_no,end='')
    print()
        

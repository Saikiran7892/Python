#hourglass shape using numbers pattern

rows=int(input('enter a number of rows:'))

middle_row=(rows//2)+1
row_no=1


while row_no<=rows:
   if row_no<=middle_row:
      for row_no in range(1,middle_row+1):
        for i in range(row_no,middle_row+1):
             print(i,end='')
        print()
        row_no+=1
   else:
      for row_no in range(row_no,row_no+1,1):
        for j in range(rows-row_no+1,middle_row+1):
            print(j,end='')
        print()
      row_no+=1

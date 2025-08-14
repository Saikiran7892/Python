
x=[1, 2, 3, 2, 1]

output=[]

for i in x:
    output=[i]+output

if x==output:
    print(True)
else:
    print(False)

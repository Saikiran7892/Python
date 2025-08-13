
#binary search

import time
x=[i for i in range(1,1000000001)]

y=999999999
s=time.time()
start=0
end=len(x)-1

while True:
    mid=(start+end)//2

    if y==x[mid]:
        print(True)
        break
    elif y>x[mid]:
        start=mid+1
    elif y<x[mid]:
        end=mid-1
    elif start>end:
        print(False)
        break
    else:
        print('code completed')

    
e=time.time()
print('Time taken is:',e-s)

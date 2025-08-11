

#checking number present in list by in operator

import time


x=[i for i in range(1,1000000001)]

y= 99999999999
start = time.time()
res=y in x
end=time.time()
print(res)
print('Time taken is:',end-start)

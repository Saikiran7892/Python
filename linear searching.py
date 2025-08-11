
#liner search

import time

x=[i for i in range(1,1000000001)]

y=99999999999

start=time.time()
for i in x:
    if i==y:
        print(True)
        break
else:
    print(False)
end=time.time()
print('Time taken is:',end-start)




import time

x={i for i in range(0,1000000) }

start=time.time()
y=99999999

if y in x:
    print('True')
else:
    print('False')
end=time.time()
print('Time taken is:',end-start)

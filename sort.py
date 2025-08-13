import time

x=[10,6,2,3,4,7,1,8,9,5]

s=time.time()
x.sort()
print(x)
end=time.time()
print('Time taken is:',end-s)

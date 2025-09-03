

#shallow copy

import copy

x=[[1,2],[3,4],5]

y=copy.copy(x)

print(id(x))
print(id(y))


print(id(x[0]))
print(id(y[0]))



x={'a':1,'b':2}
y=x.copy()
print(y)
print(id(x))
print(id(y))

print(id(x['a']))
print(id(y['a']))

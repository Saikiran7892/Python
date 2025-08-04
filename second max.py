#second max in list

x=[25,-1,23,45,-45,32,30]

first=float('-inf')
second=float('-inf')

for i in x:
    if i>first:
        first=i
x.remove(first)

for i in x:
    if i>second:
        second=i
print(second)

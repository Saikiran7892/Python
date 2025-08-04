#second max

x=[45,2,35,34,42,5]

first=float('-inf')
second=float('-inf')

for i in x:
    if i>first:
        second=first
        first=i
    if i>second and i<first:
        second=i
print(second)

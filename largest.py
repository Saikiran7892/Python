#large number in list

x=[10,20,5,90,56]
large=float('-inf')

for i in x:
    if i>large:
        large=i
print(large)

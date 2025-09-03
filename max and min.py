

d={'a':10,'b':30,'c':1}
max_value=float('-inf')
min_value=float('+inf')
max_key=None
min_key=None
for i in d.keys():
    
    if d[i] >= max_value:
        max_value=d[i]
        max_key=i
        
    if d[i] <= min_value:
        min_value=d[i]
        min_key=i

        
print(max_key,min_key)
    

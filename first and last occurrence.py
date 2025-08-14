

t=1,2,3,2,4,1,2,5,3,2,1,4

ele=int(input('enter a ele:'))

print(t.index(ele))
print(len(t)-1-t[::-1].index(ele))

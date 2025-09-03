

#vowels count in name


name=input('enter a name:')

def isvowels(st):
    vowels_cnt=0
    for ch in st:
        if ch in 'aeiouAEIOU':
            vowels_cnt+=1
    return vowels_cnt

result=isvowels(name)
print(result)

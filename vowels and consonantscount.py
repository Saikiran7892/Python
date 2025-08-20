


def isfine(st):
    v_cnt=0
    c_cnt=0
    for ch in st:
        if ch in 'aeiouAEIOU':
            v_cnt+=1
        else:
            a=ord(ch)
            if (a>=97 and a<=122) or (a>=65 and a<=90):
                c_cnt+=1
    return v_cnt,c_cnt

s="we are good students"
res=isfine(s)
print(res)

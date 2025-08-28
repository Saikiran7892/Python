


#hetrogram


s=input('enter a string:')


if len(set(s))==len(s):
    print('hetrogram')
else:
    print('Not hetrogram')

'''
for ch in s:
    if s.count(ch)>1:
       print('Not hetrogram')
       break
else:
    print('Hetrogram')
'''

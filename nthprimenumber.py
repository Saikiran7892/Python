#nth prime number

n=int(input('enter nth number:'))
num=2
cnt=0
while True:
      d=2
      while d<=num//2:
          if num%d==0:
              break
          d+=1
      else:
          cnt+=1
          if cnt==n:
              print(num)
              break
      num+=1
    

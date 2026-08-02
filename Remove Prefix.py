t=int(input())
for _ in range(t):
  n=int(input())
  a=list(map(int,input().split()))
  x=set()
  ans=0
  i=n-1
  while i >=0:
    if a[i] in x:
        ans=1+i
        break
        
        
    else:
        x.add(a[i])  
        i-=1  
  print(ans)

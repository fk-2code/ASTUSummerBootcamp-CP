t =int(input())
for _ in range(t):
 n=int(input())
 a=list(map(int,input().split()))
 p=sorted(a)

 for i in range(n-1):
  if a[i]==p[i]:
   p[i],p[i+1]=p[i+1],p[i]
 if a[n-1]==p[n-1]:
   p[n-1],p[n-2]=p[n-2],p[n-1]
 for i in range(n):
     if a[i]==p[i]:
      print(-1)
      break
 else:
         print(*(p))

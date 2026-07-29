t = int(input())

for _ in range(t):
    n, m = map(int,input().split())
    a = list(map(int,input().split()))

    maxx = max(a)
    res = []

    for _ in range(m):
        c, l, r = input().split()

        l = int(l)
        r = int(r)
        if l <= maxx and maxx <= r:
            if c == '+':
                maxx += 1
            else:
                maxx -= 1
        res.append(maxx)
    print(*res)  


  
  

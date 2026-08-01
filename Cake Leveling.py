t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    p = 0
    for i in range(n):
        p += a[i]
        if(i == 0):
            ans.append(a[i])
        else:
            x = min(ans[i-1], p // (i+1))
            ans.append(x)
    print(*(ans))

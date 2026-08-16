t = int(input())

for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    a = sorted(s, reverse=True)

    mx = a[0]
    second_mx = a[1]
    ans = []

    for x in s:
        if x == mx:
            ans.append(mx - second_mx)
        else:
            ans.append(x - mx)
    print(*ans)

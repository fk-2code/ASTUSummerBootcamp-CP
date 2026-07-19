t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    mx = 0
    for i in range(n):
        if p[i] > p[mx]:
            mx = i

    l = r = mx
    cur = n

    while cur > 1:
        found = False

        if l > 0 and p[l - 1] == cur - 1:
            l -= 1
            found = True
        elif r < n - 1 and p[r + 1] == cur - 1:
            r += 1
            found = True

        if not found:
            print("NO")
            break

        cur -= 1
    else:
        print("YES")

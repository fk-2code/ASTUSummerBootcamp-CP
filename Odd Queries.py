t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    pref = [0] * (n + 1)
    for i in range(n):
        pref[i + 1] = pref[i] + a[i]
    for _ in range(q):
        l, r, k = map(int, input().split())
        removed = pref[l-1] + (pref[n] - pref[r])
        inside = (r - l + 1) * k
        total = removed + inside
        if total % 2 == 1:
            print("YES")
        else:
            print("NO")

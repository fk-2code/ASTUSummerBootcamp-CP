t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())
    a = sorted(input())
    b = sorted(input())
    c = ""
    i = j = p = q = 0
    while i < n and j < m:
        if (a[i] < b[j] and p < k) or q == k:
            c += a[i]
            p +=1
            i += 1
            q = 0
        else:
            c += b[j]
            q += 1
            j += 1
            p = 0
    
    print(c)

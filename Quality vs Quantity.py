t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    l = 1
    r = n - 2
    sumr = a[n - 1]
    sumb = a[0]
    countr, countb = 1, 1
   
    for i in range(1, n-1)  :
        sumb += a[i]
        countb += 1
        if countr < countb and sumr > sumb:
            print("YES")
            break
        elif sumb >= sumr:
            countr += 1
            r -= 1
            sumr += a[r]

    if countr < countb and sumr > sumb:
        print("YES")
    else:
        print("NO")

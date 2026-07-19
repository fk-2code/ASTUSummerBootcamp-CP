t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    count= 0
    l = 0
    r = n - 1
    
    while l < r:
        while l < r and a[l] == 0:
            l += 1
        while l < r and a[r] == 1:
            r -= 1
        if l < r:
            count += 1
            l += 1
            r -= 1
    print(count)

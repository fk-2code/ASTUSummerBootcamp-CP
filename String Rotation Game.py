t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    ans = 0

    for  i in range(n):

        x = s[i:] + s[:i]
        count = 1
        
        for j in range(1, n):
            if x[j] != x[j - 1]:
                count += 1
        ans = max(ans, count)
    print(ans)



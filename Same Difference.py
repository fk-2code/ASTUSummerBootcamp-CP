t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    x = s[-1]
    cnt = 0

    for i in range(n - 1):
        if s[i] != x:
            cnt += 1

    print(cnt)

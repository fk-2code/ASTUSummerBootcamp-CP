t = int(input())

for _ in range(t):
    n = int(input())
    p = [0] * (2 * n + 1)

    used = [False] * (2 * n + 1)

    for i in range(1, n + 1):
        row = list(map(int, input().split()))

        for j in range(1, n + 1):
            x = row[j - 1]
            p[i + j] = x
            used[x] = True

    for x in range(1, 2 * n + 1):
        if not used[x]:
            p[1] = x
            break

    print(*p[1:])

t = int(input())

for _ in range(t):
    n = int(input())
    x = list(map(int, input().split()))
    min_pos = min(x)
    max_pos = max(x)

    ans = (max_pos - min_pos + 1) // 2
    print(ans)

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    x = 0
    for i in range(1, n - 1):
        if a[i - 1] < a[i] and a[i] > a[i + 1]:
            print("YES")
            print(i, i + 1, i + 2)
            x = 1
            break
    if x == 0:
        print("NO")

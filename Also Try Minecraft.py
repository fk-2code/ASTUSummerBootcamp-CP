n, m = map(int, input().split())
a = list(map(int, input().split()))

forward = [0] * n
for i in range(1, n):
    forward[i] = forward[i - 1]
    if a[i - 1] > a[i]:
        forward[i] += a[i - 1] - a[i]

backward = [0] * n
for i in range(n - 2, -1, -1):
    backward[i] = backward[i + 1]
    if a[i + 1] > a[i]:
        backward[i] += a[i + 1] - a[i]

for _ in range(m):
    l, r = map(int, input().split())

    if l < r:
        print(forward[r - 1] - forward[l - 1])
    else:
        print(backward[r - 1] - backward[l - 1])

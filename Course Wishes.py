t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    my_dict = {i:[] for i in range(1, k+2)}
    for idx, val in enumerate(b, start=1):
        my_dict[val].append(idx)

    ans = []

    for i in range(k, 0, -1):
        for c in my_dict[i]:
            level = i
            while level < k + 1:
                ans.append(c)
                level += 1

    print(len(ans))
    
    print(*ans)

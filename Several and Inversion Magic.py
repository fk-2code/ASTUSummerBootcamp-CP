t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    not_match = 0
    continuous = 0
    err = 1
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            not_match += 1
            continuous += err
        elif continuous:
            err = 0
    if not_match == continuous:
        print("Yes")
    else:
        print("No")

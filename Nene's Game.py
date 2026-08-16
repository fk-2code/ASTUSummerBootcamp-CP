t = int(input())
for _ in range(t):
	k, q = map(int, input().split())
	x = list(map(int, input().split()))
	n = list(map(int, input().split()))
	ans = []
	for i in range(q):
		a = min(n[i], x[0]-1)
		ans.append(a)
	print(*ans)

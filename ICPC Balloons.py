t=int(input())
for _ in range(t):
  n = int(input())
  total = 0
  sol = set()
  s = input()
  for char in s:
         if char in sol:
            total += 1
         else:
            sol.add(char)
            total += 2
  print(total)

t = int(input())
for _ in range(t):
    n, k = map(int,input().split())
    s = input()
    total = 0
    cnt = 0
    flag = True
    for c in s:
        if c=="1":
            total += 1
            cnt += 1
            if cnt >= k:
                flag = False
        else:
            cnt = 0
    if not flag:
        print("NO")
        continue


    one = 1
    zero = total+1
    ans = []
   
    for c in s:

        if c == "1":
            ans.append(one)
            one += 1
        else:
            ans.append(zero)
            zero += 1
    print("YES")
    print(*ans)

            

            
        

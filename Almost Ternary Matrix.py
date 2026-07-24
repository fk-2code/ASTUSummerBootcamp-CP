t = int(input())

for _ in range(t):
    rows, cols = map(int, input().split())

    grid = [[0] * cols for _ in range(rows)]

    for i in range(0, rows, 2):
        for j in range(0, cols, 2):
            if ((i // 2) + (j // 2)) % 2 == 0:
                grid[i][j] = 1
                grid[i][j + 1] = 0
                grid[i + 1][j] = 0
                grid[i + 1][j + 1] = 1
            else:
                grid[i][j] = 0
                grid[i][j + 1] = 1
                grid[i + 1][j] = 1
                grid[i + 1][j + 1] = 0

    for row in grid:
        print(*row)
    

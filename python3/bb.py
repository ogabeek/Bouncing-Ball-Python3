import random
import time
N = 20

map = [[0 for x in range(N)] for y in range(N)]
x, y = 1, 1 
flag = 1

x, y = 0, 0
dx, dy = 1, 2

while True:
    grid = [['.' for _ in range(N)] for _ in range(N)]
    grid[x][y] = "●"  

    for row in grid:
        print(" ".join(row))
    
    time.sleep(0.2)
    print("\033[2J\033[H", end="")

    if x == 20 or y == 20: 
        dx = random.choice([-1, 0, 1])
        dy = random.choice([-1, 0, 1])


    if x + dx < 0 or x + dx >= N:
        dx = -dx
    if y + dy < 0 or y + dy >= N:
        dy = -dy

    x += dx
    y += dy
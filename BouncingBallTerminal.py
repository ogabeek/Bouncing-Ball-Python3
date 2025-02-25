import random
import time
N = 30
num_balls = 3
balls = [[random.randint(0, N-1), random.randint(0, N-1), random.choice([-1, 1]), random.choice([-1, 1])] for _ in range(num_balls)]
while True:
    grid = [['.' for _ in range(N)] for _ in range(N)]
    for x, y, dx, dy in balls:
        grid[x][y] = "●"
    for row in grid:
        print(" ".join(row))
    time.sleep(0.1)
    print("\033[2J\033[H", end="")
    for ball in balls:
        if ball[0] + ball[2] < 0 or ball[0] + ball[2] >= N:
            ball[2] = -ball[2]
        if ball[1] + ball[3] < 0 or ball[1] + ball[3] >= N:
            ball[3] = -ball[3]
        ball[0] += ball[2]
        ball[1] += ball[3]

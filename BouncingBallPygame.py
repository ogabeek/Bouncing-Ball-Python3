import random
import pygame

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()


class Ball:
    def __init__(self, x, y, radius, color, dx, dy):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.dx = dx
        self.dy = dy

    def update(self):
        self.x += self.dx
        self.y += self.dy

        if self.x - self.radius < 0 or self.x + self.radius > width:
            self.dx = -self.dx

        if self.y - self.radius < 0 or self.y + self.radius > height:
            self.dy = -self.dy

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)


def create_balls(n):
    balls = []
    for _ in range(n):
        x = random.randint(20, width - 20)
        y = random.randint(20, height - 20)
        radius = random.randint(10, 30)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        dx = random.choice([-5, 5])
        dy = random.choice([-5, 5])
        balls.append(Ball(x, y, radius, color, dx, dy))
    return balls


def main():
    num_balls = 10
    balls = create_balls(num_balls)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 50, 200))

        for ball in balls:
            ball.update()
            ball.draw(screen)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()

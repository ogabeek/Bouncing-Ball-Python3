import pygame
import sys

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


ball = Ball(x=width//2, y=height//2, radius=20, color=(255, 0, 0), dx=5, dy=3)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ball.update()

    screen.fill((0, 60, 120))
    ball.draw(screen)
    pygame.display.flip()
    clock.tick(60)

import pygame
from paddle import Paddle

pygame.init()

WIDTH=800
HEIGHT=600

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Brick Smash")

p=Paddle(WIDTH,HEIGHT)

FPS=20
clock=pygame.time.Clock()

gameloop=True

while gameloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop=False

    p.move(event)

    screen.fill("black")
    p.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
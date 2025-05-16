import pygame
from paddle import Paddle
from ball import Ball

pygame.init()

WIDTH=800
HEIGHT=600

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Brick Smash")

padball_group=pygame.sprite.Group()

pad_group=pygame.sprite.Group()
p=Paddle(WIDTH,HEIGHT)
b=Ball(WIDTH,HEIGHT)
padball_group.add(b)
pad_group.add(p)

FPS=20
clock=pygame.time.Clock()

gameloop=True

while gameloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop=False

    pad_group.update(event)
    padball_group.update()

    screen.fill("black")
    pad_group.draw(screen)
    padball_group.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
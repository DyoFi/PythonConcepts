import pygame
from paddle import Paddle
from ball import Ball
from bricks import Bricks

pygame.init()

WIDTH=800
HEIGHT=600

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Brick Smash")

padball_group=pygame.sprite.Group()

brick_group=pygame.sprite.Group()

pad_group=pygame.sprite.Group()
p=Paddle(WIDTH,HEIGHT)
b=Ball(WIDTH,HEIGHT)
padball_group.add(b)
pad_group.add(p)

FPS=20
clock=pygame.time.Clock()

gameloop=True

start_x=50
start_y=20

Rows=6
Columns=8

x_space=10
y_space=5

for i in range(Rows):
    for j in range(Columns):
        x=start_x+j*x_space
        y=start_y+i*y_space
        b=pygame.draw.rect(screen,"Red",(x,y,80,20))
        brick_group.add(b)

while gameloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop=False

    pad_group.update(event)
    padball_group.update()
    brick_group.update()

    screen.fill("black")
    pad_group.draw(screen)
    padball_group.draw(screen)
    brick_group.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
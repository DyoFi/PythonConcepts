import pygame

pygame.init()

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Snake Game")

apple=pygame.draw.circle(screen, "Red",(500,300),10)

snake=pygame.draw.rect(screen,"Red",(400,200,20,20))
gameloop=True
while gameloop:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            gameloop=False

    screen.fill("black")
    snake=pygame.draw.rect(screen,"Red",(400,200,20,20))
    apple=pygame.draw.circle(screen, "Red",(500,300),10)
    pygame.display.flip()

pygame.quit()
import pygame

pygame.init()

screen=pygame.display.set_mode((800, 600))
pygame.display.set_caption("Dyo's Initials")

apply=pygame.draw.rect(screen, "Black", (0, 0, 0, 0))

gameloop=True
while gameloop:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            gameloop=False

    screen.fill("White")
    D=pygame.draw.rect(screen,"Black", (100, 100, 200, 400))
    ID=pygame.draw.rect(screen, "White",( 140, 140, 120, 320))
    ODU=pygame.draw.rect(screen, "White", (260, 100, 40, 40))
    ODD=pygame.draw.rect(screen, "White", (260, 460, 40, 40))

    F=pygame.draw.rect(screen, "Black", (340, 100, 200, 400))
    IFU=pygame.draw.rect(screen," White", (380, 140, 160, 100))
    IFD=pygame.draw.rect(screen, "White", (380, 280, 160, 280))
    pygame.display.flip()

pygame.quit()
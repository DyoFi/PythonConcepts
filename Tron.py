import pygame

pygame.init()

WIDTH=600
HEIGHT=600

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Tron Light Cycle")

headx=WIDTH//2
heady=HEIGHT//2

cycle_dx=0
cycle_dy=0

cycleposition=(headx,heady,20,20)

speed=10

body=[]

FPS=50
clock=pygame.time.Clock()

cycle=pygame.draw.rect(screen,"Blue",(cycleposition))

crash=pygame.mixer.Sound("C:/Users/Dyo/OneDrive/Desktop/Tron Game/Tron Crash SFX.mp3")

gameloop=True
go=False
while gameloop:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameloop=False

    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_RIGHT:
            cycle_dx=1*speed
            cycle_dy=0
        elif event.key==pygame.K_LEFT:
            cycle_dx=-1*speed
            cycle_dy=0
        elif event.key==pygame.K_UP:
            cycle_dy=-1*speed
            cycle_dx=0
        elif event.key==pygame.K_DOWN:
            cycle_dy=1*speed
            cycle_dx=0
        
    headx=headx+cycle_dx
    heady=heady+cycle_dy
    cycleposition=(headx,heady,20,20)

    body.append(cycleposition)
    
    screen.fill("black")

    for part in body:
        pygame.draw.rect(screen,"LightBlue",(part))
    cycle=pygame.draw.rect(screen,"Blue",cycleposition)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
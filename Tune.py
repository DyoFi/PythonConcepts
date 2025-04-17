import pygame

pygame.init()

WIDTH=890
HEIGHT=600

screen=pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Tune Game")

malletx=WIDTH//2
mallety=HEIGHT//2

malletposition=(malletx,mallety,20,20)

mallet=pygame.draw.rect(screen, "White", (malletposition))

speed=10

mallet_dx=0
mallet_dy=0

FPS=40
c=pygame.time.Clock()

note1=pygame.mixer.Sound("C:/Users/Dyo/OneDrive/Desktop/Tune Game/note1.mp3")
note2=pygame.mixer.Sound("C:/Users/Dyo/OneDrive/Desktop/Tune Game/note2.mp3")
note3=pygame.mixer.Sound("C:/Users/Dyo/OneDrive/Desktop/Tune Game/note3.mp3")
noteA=pygame.mixer.Sound("C:/Users/Dyo/OneDrive/Desktop/Tune Game/noteA.mp3")
noteB=pygame.mixer.Sound("C:/Users/Dyo/OneDrive/Desktop/Tune Game/noteB.mp3")
noteC=pygame.mixer.Sound("C:/Users/Dyo/OneDrive/Desktop/Tune Game/noteC.mp3")
noteD=pygame.mixer.Sound("C:/Users/Dyo/OneDrive/Desktop/Tune Game/noteD.mp3")
noteE=pygame.mixer.Sound("C:/Users/Dyo/OneDrive/Desktop/Tune Game/noteE.mp3")


gameloop=True
while gameloop:
    screen.fill("black")
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameloop=False
        
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_UP:
            mallet_dy=-1*speed
            mallet_dx=0
        elif event.key==pygame.K_DOWN:
            mallet_dy=1*speed
            mallet_dx=0
        elif event.key==pygame.K_RIGHT:
            mallet_dx=1*speed
            mallet_dy=0
        elif event.key==pygame.K_LEFT:
            mallet_dx=-1*speed
            mallet_dy=0

    malletx=malletx+mallet_dx
    mallety=mallety+mallet_dy
    malletposition=(malletx,mallety,20,20)

    Red=pygame.draw.rect(screen,"Red",(10,10,100,550))
    Orange=pygame.draw.rect(screen,"Orange",(120,10,100,510))
    Yellow=pygame.draw.rect(screen,"Yellow",(230,10,100,470))
    Green=pygame.draw.rect(screen,"Green",(340,10,100,430))
    Blue=pygame.draw.rect(screen,"Blue",(450,10,100,390))
    Purple=pygame.draw.rect(screen,"Purple",(560,10,100,350))
    Pink=pygame.draw.rect(screen,"Pink",(780,10,100,270))
    Violet=pygame.draw.rect(screen,"Violet",(670,10,100,310))

    mallet=pygame.draw.rect(screen, "White", (malletposition))

    if mallet.colliderect(Red):
        note1.play()
    if mallet.colliderect(Orange):
        note2.play()
    if mallet.colliderect(Yellow):
        note3.play()
    if mallet.colliderect(Green):
        noteA.play()
    if mallet.colliderect(Blue):
        noteB.play()
    if mallet.colliderect(Purple):
        noteC.play()
    if mallet.colliderect(Violet):
        noteD.play()
    if mallet.colliderect(Pink):
        noteE.play()
    
    pygame.display.flip()
    c.tick(FPS)

pygame.quit()
import pygame
from paddle import Paddle
from ball import Ball
from bricks import Bricks

pygame.init()

WIDTH=800
HEIGHT=600

rbrick=pygame.image.load("C:/Users/Dyo/OneDrive/Desktop/Brick Smash/1615227106_10594-removebg-preview.png")
bbrick=pygame.image.load("C:/Users/Dyo/OneDrive/Desktop/Brick Smash/R-removebg-preview.png")
gbrick=pygame.image.load("C:/Users/Dyo/OneDrive/Desktop/Brick Smash/green-7245648_1280-removebg-preview.png")
ybrick=pygame.image.load("C:/Users/Dyo/OneDrive/Desktop/Brick Smash/OIP-removebg-preview (2).png")

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

T=pygame.font.Font(None,36)
L=pygame.font.SysFont("Comic Sans MS",36)

start_x=80
start_y=60

Rows=7
Columns=7

x_space=100
y_space=40

gameover = False
gamewin=False

for i in range(Rows):
    for j in range(Columns):
        x=start_x+j*x_space
        y=start_y+i*y_space
        bricks=Bricks(x,y,7)
        brick_group.add(bricks)

while gameloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop=False

    if len(brick_group) == 0:
        gamewin_text=L.render("Congratulations!", True, ("Green"))
        gamewin_rect=gamewin_text.get_rect(centerx=WIDTH//2,centery=HEIGHT//2)
        gamewin=True

    if gamewin:
        screen.fill("White")
        screen.blit(gamewin_text,gamewin_rect)
        pygame.display.update()
        pygame.time.delay(2000)
        gameloop=False

    if b.rect.bottom >= HEIGHT:
        gameover_text=L.render("Game Over!", True, ("Red"))
        gameover_rect=gameover_text.get_rect(centerx=WIDTH//2,centery=HEIGHT//2)
        gameover=True
    
    if gameover:
        screen.fill("black")
        screen.blit(gameover_text,gameover_rect)
        pygame.display.update()
        pygame.time.delay(2000)
        gameloop=False

    pad_group.update(event)
    padball_group.update()
    brick_group.update()

    screen.fill("black")

    score_text=T.render("Score =" +str(p.score), True, ("Green"))
    score_rect=score_text.get_rect(centerx=600,centery=50)
    screen.blit(score_text,score_rect)

    pygame.draw.line(screen,"White",(0,500),(800,500), 1)


    for br in brick_group:
        if b.rect.colliderect(br.rect):
            dx=b.rect.centerx - br.rect.centerx
            dy=b.rect.centery - br.rect.centery

            overlap_x = (br.rect.width//2 + b.rect.width//2)-abs(dx)
            overlap_y = (br.rect.height//2 + b.rect.height//2)-abs(dy)

            if overlap_x < overlap_y:
                b.speed_x*=-1
                if dx >0:
                    b.rect.left=br.rect.right
                else:
                    b.rect.right=br.rect.left
            else:
                b.speed_y*=-1
                if dy > 0:
                    b.rect.top=br.rect.bottom
                else:
                    b.rect.bottom=br.rect.top
        
            brick_group.remove(br)

            p.score+=10

            break

    if b.rect.colliderect(p.rect):
        b.speed_y*=-1

    pygame.display.update()

    pad_group.draw(screen)
    padball_group.draw(screen)
    brick_group.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
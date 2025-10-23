import pygame
import sys
import pymunk
import pymunk.pygame_util
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Balloon Buster Game")

balloon_image = pygame.image.load("C:/Users/Dyo/OneDrive/Desktop/Balloon Popper/balloon.png")
balloon_image = pygame.transform.scale(balloon_image, (100,100))

bg_image = pygame.image.load("C:/Users/Dyo/OneDrive/Desktop/Balloon Popper/balloonbg.jpg")
bg_image = pygame.transform.scale(bg_image, (800,600))

balloon_pop = pygame.mixer.Sound("C:/Users/Dyo/OneDrive/Desktop/Balloon Popper/party-balloon-pop-323588.mp3")

t = pygame.font.SysFont("Arial", 36)
r = pygame.font.SysFont("Arial", 77)

score = 0

balloons = []

# Set up clock and frame rate
clock = pygame.time.Clock()
FPS = 60

frame_count = 0
max_frame = 900

go = False
gw = False

space=pymunk.Space()
space.gravity = (0,-300)
draw_option = pymunk.pygame_util.DrawOptions(screen)

def create_balloon():
    x = random.randint(50,750)
    y = 550
    body=pymunk.Body(1, pymunk.moment_for_circle(1,0,1))
    body.position = x,y
    shape = pymunk.Circle(body,1)
    shape.elasticity = 0.2
    shape.friction = 0.5
    shape.color = (255,0,0,255)
    space.add(body,shape)
    return body,shape

# Game loop to keep the window open
running = True
while running:

    screen.blit(bg_image, (0, 0))
    
    target_score = 20

    if random.randint(1,30) == 1:
        balloons.append(create_balloon())

    for body,shape in balloons:
        x,y = body.position
        screen.blit(balloon_image, (x-50,y-25))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            mouse_rect = pygame.Rect(mouse_pos[0], mouse_pos[1],1,1)

            for body,shape in balloons:
                x,y=body.position
                balloon_rect = pygame.Rect(x-50,y-25, 100,100)

                if balloon_rect.colliderect(mouse_rect):
                    balloons.remove((body,shape))
                    space.remove (body,shape)
                    balloon_pop.play()
                    score+=1

                    if score >= target_score:
                        gw = True
    
    if gw == True:
        screen.fill("black")
        screen.blit(gw_text, (225,250))
        pygame.display.update()
        pygame.time.delay(2000)
        pygame.quit()

    if go == True:
        screen.fill("black")
        screen.blit(go_text, (200,250))
        pygame.display.update()
        pygame.time.delay(2000)
        pygame.quit()

    if go == False:
        frame_count+=1
        time_left = (max_frame - frame_count) // 60
        time_text = t.render("Timer =" +str(time_left), True, "Red")
        screen.blit(time_text, (50,30))
        if frame_count >= max_frame:
            go = True


    score_text = t.render("Score ="+str(score), True, "Green")

    go_text = r.render("GAME OVER", True, "Red")
    gw_text = r.render("YOU WON", True, "Purple")

    screen.blit(score_text, (650, 30))

    space.debug_draw(draw_option)
    space.step(1/60)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()

import pygame
import pymunk
import pymunk.pygame_util

pygame.init()

HEIGHT = 600
WIDTH = 800

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Angry Birds")

space = pymunk.Space()
space.gravity = (0,981)
draw_option = pymunk.pygame_util.DrawOptions(screen)

score = 0

attempts = 3

lose_sound = pygame.mixer.Sound("C:/Users/Dyo/OneDrive/Desktop/Physics Pymunk\Angry Bird Game/lose.mp3")

hit_sound = pygame.mixer.Sound("C:/Users/Dyo/OneDrive/Desktop/Physics Pymunk/Angry Bird Game/hit (1).mp3")

launch_sound = pygame.mixer.Sound("C:/Users/Dyo/OneDrive/Desktop/Physics Pymunk/Angry Bird Game/launch.mp3")

bird_image = pygame.image.load("C:/Users/Dyo/OneDrive/Desktop/Physics Pymunk/Angry Bird Game/bird.png")
bird_image = pygame.transform.scale(bird_image, (40,40))

wood_image = pygame.image.load("C:/Users/Dyo/OneDrive/Desktop/Physics Pymunk/Angry Bird Game/wood1.png")
wood_image = pygame.transform.scale(wood_image, (60,60))

pig_image = pygame.image.load("C:/Users/Dyo/OneDrive/Desktop/Physics Pymunk/Angry Bird Game/pig.png")
pig_image = pygame.transform.scale(pig_image, (40,40))

bg_image = pygame.image.load("C:/Users/Dyo\OneDrive/Desktop/Physics Pymunk/Angry Bird Game/background.jpg")
bg_image = pygame.transform.scale(bg_image, (800,600))

go = False

gameloop=True

def create_ball(x,y):
    body = pymunk.Body(1, pymunk.moment_for_circle(1,0,10))
    body.position = (x,y)
    shape = pymunk.Circle(body,10)
    shape.elasticity = 0.3
    shape.friction = 0.5
    space.add(body,shape)
    return(body,shape)

ball_body, ball_shape = create_ball(150,100)


ground_body = pymunk.Body(body_type = pymunk.Body.STATIC)
ground_body.shape= pymunk.Segment(ground_body, (0,600),(800,600),10)
ground_body.shape.friction = 0.5
space.add(ground_body, ground_body.shape)

def create_block(x,y):
    body = pymunk.Body(1, pymunk.moment_for_box(1, (60,60)))
    body.position = x,y
    shape = pymunk.Poly.create_box(body, (60,60))
    shape.elasticity = 0.4
    shape.friction = 0.6
    space.add(body,shape)
    return(body,shape)

def create_pig(x,y):
    body = pymunk.Body(1, pymunk.moment_for_circle(1, 0, 20))
    body.position = x,y
    shape = pymunk.Circle(body, 20)
    shape.elasticity = 0.4
    shape.friction = 0.6
    space.add(body,shape)
    return(body,shape)

blocks = [create_block(600,550), create_block(600,490), create_block(660,550),create_block(540,550), create_block(540,490), create_block(540,430)]

pigs = [create_pig(550,390), create_pig(540, 390)]

def draw_objects():
    global score
    global go
    screen.blit(bg_image, (0,0))

    s = pygame.font.SysFont("Comic Sans MS", 24)
    w = pygame.font.SysFont("Arial", 60)

    w_text = w.render("YOU WIN!", True, "Yellow")

    score_text = s.render("Score =" +str(score), True, "Green")
    screen.blit(score_text,(650,20))

    att_text = s.render("Attempts =" +str(attempts), True, "Red")
    screen.blit(att_text, (650,50))

    bod_position = ball_body.position
    screen.blit(bird_image, (bod_position.x-20, bod_position.y-20))
    for body,shape in blocks:
        block_pos = body.position
        angle = body.angle*(180/3.1415)
        rotate_brick = pygame.transform.rotate(wood_image, angle)
        rect = rotate_brick.get_rect(center = (block_pos.x, block_pos.y))
        screen.blit(rotate_brick, rect.topleft)
    for body,shape in pigs:
        pig_pos = body.position
        screen.blit(pig_image, (pig_pos.x-20,pig_pos.y-20))
        if pig_pos.x >800:
            pigs.remove((body,shape))
            space.remove(body,shape)
            score = score+1
    if score == 2:
        screen.blit(w_text, (300,275))
        
    if attempts == 0:
        go=True


FPS = 20

clock = pygame.time.Clock()

while gameloop:
    for event in pygame.event.get():

        w = pygame.font.SysFont("Arial", 60)
        go_text = w.render("GAME OVER!", True, "Red")

        if event.type == pygame.QUIT:
            gameloop=False

        if pygame.sprite.collide_rect(ball_body, pigs):
            hit_sound.play()


        elif event.type ==pygame.MOUSEBUTTONDOWN and attempts>0:
            mouse_pos = pygame.mouse.get_pos()
            ball_body.pos = (150,500)
            velocity_x = (mouse_pos[0] - 150)*4
            velocity_y = (mouse_pos[1] - 500)*4
            ball_body.velocity = velocity_x, velocity_y
            attempts = attempts-1
            launch_sound.play()

        if go == True:
            screen.blit(go_text, (300,275))
            lose_sound.play()
            pygame.time.delay(2000)
            gameloop = False
    
            

    space.step(1/60)
    draw_objects()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
import pygame

# Initialize pygame
pygame.init()

# Set display surface
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Paddle Game")

#load the sound and play it when required
hit_sound = pygame.mixer.Sound("C:/Users/Dyo/OneDrive/Desktop/Ping Pong Challenge/hit.mp3")
gameover_sound = pygame.mixer.Sound("C:/Users/Dyo/OneDrive/Desktop/Ping Pong Challenge/game_over.mp3")

# Set FPS and clock
FPS = 60
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)  # Default font, size 36
# Colors
WHITE = (255, 255, 255)

class PlayerPaddle(pygame.sprite.Sprite):
    def __init__(self, x, y, is_player=True):
        super().__init__()
        self.image = pygame.Surface((20, 100))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocity = 8
        self.score= 0
    
    def update(self):
       
        #write the code for the player to move
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.rect.y-=self.velocity
            if event.key == pygame.K_DOWN:
                self.rect.y+=self.velocity

class ComputerPaddle(pygame.sprite.Sprite):
    def __init__(self, x, y, is_player=True):
        super().__init__()
        self.image = pygame.Surface((20, 100))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocity = 8
        self.score=0
    
    def update(self):
        #write the code for the computer paddle movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.y-=self.velocity
        if keys[pygame.K_s]:
            self.rect.y+=self.velocity

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocity_x = 3
        self.velocity_y = 3
    
    def update(self):
       #write the code for ball movement
       self.rect.x+=self.velocity_x
       self.rect.y+=self.velocity_y

       #write the code for the bounce off condition
       if pygame.sprite.collide_rect(ball,player_paddle):
           self.velocity_x*=1.25
           self.velocity_y*=1.25
           self.velocity_x*=-1
           hit_sound.play()

       if pygame.sprite.collide_rect(ball,computer_paddle):
           self.velocity_x+=1.25
           self.velocity_y+=1.25
           self.velocity_x*=-1
           hit_sound.play()

       if self.rect.top <= 0 or self.rect.bottom >= WINDOW_HEIGHT:
           self.velocity_y*=-1
           hit_sound.play()

# Create game objects
player_paddle = PlayerPaddle(30, WINDOW_HEIGHT//2, is_player=True)
computer_paddle = ComputerPaddle(WINDOW_WIDTH-50, WINDOW_HEIGHT//2, is_player=False)
ball = Ball(WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

# Create sprite groups
all_sprites = pygame.sprite.Group()
all_sprites.add(player_paddle, computer_paddle, ball)

# Main game loop
running = True
gameover=False
gamewin=False

f = pygame.font.SysFont("Comic Sans MS", 36)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update objects
    player_paddle.update()
    computer_paddle.update()
    ball.update()


    player_score_text = font.render(f"Player Score: {player_paddle.score}", True, WHITE)
    player_score_rect = player_score_text.get_rect(topleft=(10, 10)) 

    computer_score_text = font.render(f"Computer Score: {computer_paddle.score}", True, WHITE)
    computer_score_rect = computer_score_text.get_rect(topright=(780, 10)) 


    gameover_text = font.render(f"Game Over", True, WHITE)
    gameover_rect = gameover_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))

    gamewin_text = font.render(f"You Win!", True, WHITE)
    gamewin_rect = gamewin_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))


    #Write the conditions if the ball goes out of bound
    if ball.rect.x <= 0:
        computer_paddle.score+=1
        ball.rect.centerx=WINDOW_WIDTH//2
        ball.rect.centery=WINDOW_HEIGHT//2
        ball.velocity_x=3
        ball.velocity_y=3
        ball.velocity_x*=-1
    
    if ball.rect.x >= WINDOW_WIDTH:
        player_paddle.score+=1
        ball.rect.centerx=WINDOW_WIDTH//2
        ball.rect.centery=WINDOW_HEIGHT//2
        ball.velocity_x=3
        ball.velocity_y=3
        ball.velocity_x*=-1

    #write gameover condition
    if player_paddle.score >= 5:
        gamewin=True
    
    if gamewin:
        display_surface.fill("black")
        display_surface.blit(gamewin_text, gamewin_rect)
        pygame.display.update()
        pygame.time.delay(2000)
        running=False

    if computer_paddle.score >= 2:
        gameover=True

    if gameover:
        display_surface.fill("black")
        display_surface.blit(gameover_text, gameover_rect)
        pygame.display.update()
        pygame.time.delay(2000)
        running=False
        gameover_sound.play()

    #Write Ball collision with paddles condition
   
   
    # Draw everything
    display_surface.fill((0,0,0))
    all_sprites.draw(display_surface)

    display_surface.blit(player_score_text, player_score_rect)
    display_surface.blit(computer_score_text, computer_score_rect)
    pygame.display.update()
    clock.tick(FPS)
    
pygame.quit()

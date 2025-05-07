import pygame

class Paddle:
    def __init__(self,WIDTH,HEIGHT):
        self.rect = pygame.Rect(WIDTH//2, HEIGHT-30, 100, 20)
        self.velocity=10
    
    def move(self, event):
        if event.type==pygame.KEYDOWN:
            if self.rect.left>0:
                if event.key==pygame.K_LEFT:
                    self.rect.x=self.rect.x-self.velocity
            if self.rect.right<800:
                if event.key==pygame.K_RIGHT:
                    self.rect.x=self.rect.x+self.velocity
    def draw(self,screen):
        pygame.draw.rect(screen,"Red",(self.rect))

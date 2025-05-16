import pygame

class Paddle(pygame.sprite.Sprite):
    def __init__(self,WIDTH, HEIGHT):
        super().__init__()
        self.image=pygame.image.load("C:/Users/Dyo/OneDrive/Desktop/Brick Smash/R-removebg-preview.png")
        self.image=pygame.transform.scale(self.image, (100,20))
        self.rect=self.image.get_rect()
        self.rect.x=WIDTH//2
        self.rect.y=HEIGHT-40
        self.velocity=10
    
    def update(self, event):
        if event.type==pygame.KEYDOWN:
            if self.rect.left>0:
                if event.key==pygame.K_LEFT:
                    self.rect.x=self.rect.x-self.velocity
            if self.rect.right<800:
                if event.key==pygame.K_RIGHT:
                    self.rect.x=self.rect.x+self.velocity


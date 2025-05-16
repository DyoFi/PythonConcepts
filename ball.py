import pygame

WIDTH=800
HEIGHT=600

class Ball(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image=pygame.image.load("C:/Users/Dyo/OneDrive/Desktop/Brick Smash/Red Circle for Brick Smash.png")
        self.image=pygame.transform.scale(self.image, (20,20))
        self.rect=self.image.get_rect()
        self.rect.centerx=WIDTH//2
        self.rect.centery=HEIGHT//2
        self.speed_x=5
        self.speed_y=-5

    def update(self):
        self.rect.x=self.rect.x+self.speed_x
        self.rect.y=self.rect.y+self.speed_y
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speed_x *=-1
        if self.rect.top <=0 or self.rect.bottom >=HEIGHT:
            self.speed_y *=-1
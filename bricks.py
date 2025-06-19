import pygame
import random

rbrick=pygame.image.load("C:/Users/Dyo/OneDrive/Desktop/Brick Smash/1615227106_10594-removebg-preview.png")
bbrick=pygame.image.load("C:/Users/Dyo/OneDrive/Desktop/Brick Smash/R-removebg-preview.png")
gbrick=pygame.image.load("C:/Users/Dyo/OneDrive/Desktop/Brick Smash/green-7245648_1280-removebg-preview.png")
ybrick=pygame.image.load("C:/Users/Dyo/OneDrive/Desktop/Brick Smash/OIP-removebg-preview (2).png")

bricks = ["C:/Users/Dyo/OneDrive/Desktop/Brick Smash/1615227106_10594-removebg-preview.png", "C:/Users/Dyo/OneDrive/Desktop/Brick Smash/R-removebg-preview.png", "C:/Users/Dyo/OneDrive/Desktop/Brick Smash/green-7245648_1280-removebg-preview.png", "C:/Users/Dyo/OneDrive/Desktop/Brick Smash/OIP-removebg-preview (2).png"]

class Bricks(pygame.sprite.Sprite):
    def __init__(self,x,y, brick_group):
        super().__init__()
        bricks = ["C:/Users/Dyo/OneDrive/Desktop/Brick Smash/1615227106_10594-removebg-preview.png", "C:/Users/Dyo/OneDrive/Desktop/Brick Smash/R-removebg-preview.png", "C:/Users/Dyo/OneDrive/Desktop/Brick Smash/green-7245648_1280-removebg-preview.png", "C:/Users/Dyo/OneDrive/Desktop/Brick Smash/OIP-removebg-preview (2).png"]
        self.image = pygame.image.load(bricks[random.randint(0,3)])
        self.image=pygame.transform.scale(self.image,(70,50))
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        self.brick_group=brick_group


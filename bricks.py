import pygame
import random

class Bricks(pygame.sprite.Sprite):
    def __init__(self,screen,x,y):
        super().__init__()
        colours=["red","blue","green","yellow","orange"]
        self.image=pygame.draw.rect(screen,random.choice(colours),(x,y,80,20))

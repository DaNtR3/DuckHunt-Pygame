import pygame
import random


class Dog:
    def __init__(self):
        self.load = pygame.image.load("assets/dog.png")
        self.scale = pygame.transform.scale(self.load, (120, 120))
        self.x = random.randint(0, 1280)
        self.y = random.randint(455, 455)

    def render_dog(self, display):
        display.blit(self.scale, (self.x, self.y))

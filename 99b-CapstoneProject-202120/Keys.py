import pygame
import sys
import time
import math

class Keys:
    def __init__(self, screen, x, y, image, speed):
        self.key_image = image
        self.image = pygame.image.load(image)
        self.image_scaled = pygame.transform.scale(self.image, (50, 55))
        self.x = x
        self.y = y
        self.screen = screen
        self.speed = speed
        self.keys_collected = 0
        self.collected = False

    def collect_key(self, cat):
        if self.collected == False:
            distance = math.sqrt((self.x - cat.x) ** 2 + (self.y - cat.y) ** 2)
            if distance <= 45:
                self.collected = True
                self.keys_collected = 1
        return self.keys_collected


    def catch_em_all(self, dogs):
            for dog in dogs:
                dog.radius = 1000

    def draw(self):
        if self.collected == False:
            self.screen.blit(self.image_scaled, (self.x, self.y))


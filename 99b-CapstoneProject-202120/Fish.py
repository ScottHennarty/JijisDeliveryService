import pygame
import sys
import time
import math

class Fishes:
    def __init__(self, screen, x, y, refill):
        self.screen = screen
        self.x = x
        self.y = y
        self.refill = refill
        self.image = pygame.image.load("Sturgeon.png")
        self.image_scaled = pygame.transform.scale(self.image, (40, 45))
        self.eaten = False
        self.eating_sound = pygame.mixer.Sound("Sounds/Eating Sound.wav")

    def eat_fish(self, stamina, cat):
        if self.eaten == False:
            distance = math.sqrt((self.x - cat.x) ** 2 + (self.y - cat.y) ** 2)
            if distance <= 45:
                self.eating_sound.play()
                self.eaten = True
                stamina.width = stamina.width + self.refill
                if stamina.width > stamina.width_origional:
                    stamina.width = stamina.width_origional

    def draw(self):
        if self.eaten == False:
            self.screen.blit(self.image_scaled, (self.x, self.y))





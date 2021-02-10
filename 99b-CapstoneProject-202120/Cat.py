import pygame
import sys
import time
import math

class Cat:
    def __init__(self, screen):
        """ The cat sets the speed and is place in the center of the screen """
        self.screen = screen
        self.x = self.screen.get_width() // 2 - 50
        self.y = self.screen.get_height() // 2 - 50
        self.standing_image = pygame.image.load("Cute_Kitten.png")
        self.speed = 3

    def draw(self):
        self.screen.blit(self.standing_image, (self.x, self.y))
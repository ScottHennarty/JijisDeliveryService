import pygame
import sys
import time
import math

class Dog:
    def __init__(self, screen, x, y):
        """ A dog will run towards the center unless he is a certain radius away from the center """
        self.screen = screen
        self.x = x
        self.y = y
        self.standing_image = pygame.image.load("Definetly_A_Dog.png")
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        self.radius = 400

    def draw(self):
        self.screen.blit(self.standing_image, (self.x, self.y))

    def move(self):
        distance_x = (self.screen_width // 2) - self.x
        distance_y = (self.screen_height // 2) - self.y
        magnitude = math.sqrt(distance_x ** 2 + distance_y ** 2)
        if magnitude <= self.radius:
            if distance_x > 0:
                self.x = self.x + 2
            if distance_x < 0:
                self.x = self.x - 2
            if distance_y > 0:
                self.y = self.y + 2
            if distance_y < 0:
                self.y = self.y - 2
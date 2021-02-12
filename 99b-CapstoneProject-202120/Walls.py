import pygame
import sys
import time
import math

class Walls:
    def __init__(self, screen, x, y, width, height, color, speed):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        self.speed = speed
        self.speed_reset()

    def speed_reset(self):
        self.x_speed_right = self.speed
        self.x_speed_left = self.speed
        self.y_speed_up = self.speed
        self.y_speed_down = self.speed

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT]:
            self.x = self.x + self.x_speed_right
        if pressed_keys[pygame.K_RIGHT]:
            self.x = self.x - self.x_speed_left
        if pressed_keys[pygame.K_UP]:
            self.y = self.y + self.y_speed_up
        if pressed_keys[pygame.K_DOWN]:
            self.y = self.y - self.y_speed_down





import pygame
import sys
import time
import math

class Stamina:
    def __init__(self, screen, width, height, speed, level):
        self.screen = screen
        self.width_origional = width
        self.width = width
        self.height = height
        self.speed = speed
        self.level = level
        self.BLACK = pygame.Color("Black")
        self.font1 = pygame.font.Font(None, 28)
        self.font2 = pygame.font.Font(None, 40)
        self.caption1 = self.font1.render("Stamina", True, self.BLACK)
        self.caption2 = self.font2.render("Level:", True, self.BLACK)
        self.caption3 = self.font2.render(str(level), True, self.BLACK)
        self.time = 0
        self.time_delayer = 0

    def draw(self):
        pygame.draw.rect(self.screen, (0, 204, 0), (40, 700, self.width, self.height))
        self.screen.blit(self.caption1, (45, 670))
        self.screen.blit(self.caption2, (35, 45))
        self.screen.blit(self.caption3, (125, 45))


    def drain(self):
        if self.time_delayer % 7 == 0:
            self.time = self.time + 1
            if self.time % 2 == 0:
                self.width = self.width - self.speed
        self.time_delayer = self.time_delayer + 1

    def game_over(self, cat):
        if self.width <= 0:
            cat.game_over_sound.play()
            return True
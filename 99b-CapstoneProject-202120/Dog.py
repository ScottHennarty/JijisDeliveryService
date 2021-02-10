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
        self.standing_right_1 = pygame.image.load("El Perro/Dog_Right_Idle_1.png")
        self.standing_right_2 = pygame.image.load("El Perro/Dog_Right_Idle_2.png")
        self.standing_left_1 = pygame.image.load("El Perro/Dog_Left_Idle_1.png")
        self.standing_left_2 = pygame.image.load("El Perro/Dog_Left_Idle_2.png")
        self.right_run_1 = pygame.image.load("El Perro/Dog_Right_Run_1.png")
        self.right_run_2 = pygame.image.load("El Perro/Dog_Right_Run_2.png")
        self.right_run_3 = pygame.image.load("El Perro/Dog_Right_Run_3.png")
        self.left_run_1 =  pygame.image.load("El Perro/Dog_Left_Run_1.png")
        self.left_run_2 = pygame.image.load("El Perro/Dog_Left_Run_2.png")
        self.left_run_3 = pygame.image.load("El Perro/Dog_Left_Run_3.png")
        self.time = 0
        self.time_delayer = 0
        self.one_or_two = 0
        self.radius = 400
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()

    def draw(self):
        if self.magnitude <= self.radius:
            if (self.screen_width // 2) - self.x > 0:
                if self.time_delayer % 9 == 0:
                    self.time = self.time + 1
                if self.time % 2 == 0:
                    if self.one_or_two % 2 == 0:
                        self.screen.blit(self.right_run_3, (self.x, self.y))
                    else:
                        self.screen.blit(self.right_run_1, (self.x, self.y))
                else:
                    self.screen.blit(self.right_run_2, (self.x, self.y))
                    self.one_or_two = self.one_or_two + 1
                self.time_delayer = self.time_delayer + 1
            elif(self.screen_width // 2) - self.x <= 0:
                if self.time_delayer % 9 == 0:
                    self.time = self.time + 1
                if self.time % 2 == 0:
                    if self.one_or_two % 2 == 0:
                        self.screen.blit(self.left_run_3, (self.x, self.y))
                    else:
                        self.screen.blit(self.left_run_1, (self.x, self.y))
                else:
                    self.screen.blit(self.left_run_2, (self.x, self.y))
                    self.one_or_two = self.one_or_two + 1
                self.time_delayer = self.time_delayer + 1
        else:
            if (self.screen_width // 2) - self.x > 0:
                if self.time_delayer % 13 == 0:
                    self.time = self.time + 1
                if self.time % 2:
                    self.screen.blit(self.standing_right_1, (self.x, self.y))
                else:
                    self.screen.blit(self.standing_right_2, (self.x + 4, self.y + 2))
                self.time_delayer = self.time_delayer + 1
            else:
                if self.time_delayer % 13 == 0:
                    self.time = self.time + 1
                if self.time % 2:
                    self.screen.blit(self.standing_left_1, (self.x, self.y))
                else:
                    self.screen.blit(self.standing_left_2, (self.x + 2, self.y + 2))
                self.time_delayer = self.time_delayer + 1




    def move(self):
        distance_x = (self.screen_width // 2) - self.x
        distance_y = (self.screen_height // 2) - self.y
        self.magnitude = math.sqrt(distance_x ** 2 + distance_y ** 2)
        if self.magnitude <= self.radius:
            if distance_x > 0:
                self.x = self.x + 2
            if distance_x < 0:
                self.x = self.x - 2
            if distance_y > 0:
                self.y = self.y + 2
            if distance_y < 0:
                self.y = self.y - 2
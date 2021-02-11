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
        self.standing_left_1 = pygame.image.load("New Perro/Dog_Left_Idle_1.png")
        self.standing_left_1_scaled = pygame.transform.scale(self.standing_left_1, (70, 65))
        self.standing_right_1 = pygame.image.load("New Perro/Dog_Right_Idle_1.png")
        self.standing_right_1_scaled = pygame.transform.scale(self.standing_right_1, (70, 65))
        self.left_run_1 = pygame.image.load("New Perro/Dog_Left_Walk_1.png")
        self.left_run_1_scaled = pygame.transform.scale(self.left_run_1, (70, 65))
        self.left_run_2 = pygame.image.load("New Perro/Dog_Left_Walk_2.png")
        self.left_run_2_scaled = pygame.transform.scale(self.left_run_2, (70, 65))
        self.left_run_3 = pygame.image.load("New Perro/Dog_Left_Walk_3.png")
        self.left_run_3_scaled = pygame.transform.scale(self.left_run_3, (70, 65))
        self.right_run_1 = pygame.image.load("New Perro/Dog_Right_Walk_1.png")
        self.right_run_1_scaled = pygame.transform.scale(self.right_run_1, (70, 65))
        self.right_run_2 = pygame.image.load("New Perro/Dog_Right_Walk_2.png")
        self.right_run_2_scaled = pygame.transform.scale(self.right_run_2, (70, 65))
        self.right_run_3 = pygame.image.load("New Perro/Dog_Right_Walk_3.png")
        self.right_run_3_scaled = pygame.transform.scale(self.right_run_3, (70, 65))
        self.time = 0
        self.time_delayer = 0
        self.one_or_two = 0
        self.radius = 400
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        self.speed = 2

    def draw(self):
        if self.magnitude <= self.radius:
            if (self.screen_width // 2) - self.x - 35 > 15:
                if self.time_delayer % 11 == 0:
                    self.time = self.time + 1
                if self.time % 2 == 0:
                    if self.one_or_two % 2 == 0:
                        self.screen.blit(self.right_run_3_scaled, (self.x, self.y))
                    else:
                        self.screen.blit(self.right_run_1_scaled, (self.x, self.y))
                else:
                    self.screen.blit(self.right_run_2_scaled, (self.x, self.y))
                    self.one_or_two = self.one_or_two + 1
                self.time_delayer = self.time_delayer + 1
            elif(self.screen_width // 2) - self.x - 35 < -15:
                if self.time_delayer % 11 == 0:
                    self.time = self.time + 1
                if self.time % 2 == 0:
                    if self.one_or_two % 2 == 0:
                        self.screen.blit(self.left_run_3_scaled, (self.x, self.y))
                    else:
                        self.screen.blit(self.left_run_1_scaled, (self.x, self.y))
                else:
                    self.screen.blit(self.left_run_2_scaled, (self.x, self.y))
                    self.one_or_two = self.one_or_two + 1
                self.time_delayer = self.time_delayer + 1
            #Here I will be adding up and down animations in an else loop but I need to do other work right now
        else:
            if (self.screen_width // 2) - self.x > 0:
                    self.screen.blit(self.standing_right_1_scaled, (self.x, self.y))
            else:
                    self.screen.blit(self.standing_left_1_scaled, (self.x, self.y))




    def move(self):
        distance_x = (self.screen_width // 2) - self.x - 45
        distance_y = (self.screen_height // 2) - self.y - 45
        self.magnitude = math.sqrt(distance_x ** 2 + distance_y ** 2)
        if self.magnitude <= self.radius:
            if distance_x > -1:
                self.x = self.x + self.speed
            if distance_x < 1:
                self.x = self.x - self.speed
            if distance_y > -1:
                self.y = self.y + self.speed
            if distance_y < 1:
                self.y = self.y - self.speed
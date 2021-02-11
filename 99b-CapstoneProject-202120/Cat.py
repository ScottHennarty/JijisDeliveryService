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
        self.standing_left_1 = pygame.image.load("New Gato/Cat_Left_Idle_1.png")
        self.standing_left_1_scaled = pygame.transform.scale(self.standing_left_1, (65, 60))
        self.standing_right_1 = pygame.image.load("New Gato/Cat_Right_Idle_1.png")
        self.standing_right_1_scaled = pygame.transform.scale(self.standing_right_1, (65, 60))
        self.left_run_1 = pygame.image.load("New Gato/Cat_Left_Walk_2.png")
        self.left_run_1_scaled = pygame.transform.scale(self.left_run_1, (65, 60))
        self.left_run_2 = pygame.image.load("New Gato/Cat_Left_Walk_2.png")
        self.left_run_2_scaled = pygame.transform.scale(self.left_run_2, (65, 60))
        self.right_run_1 = pygame.image.load("New Gato/Cat_Right_Walk_1.png")
        self.right_run_1_scaled = pygame.transform.scale(self.right_run_1, (65, 60))
        self.right_run_2 = pygame.image.load("New Gato/Cat_Right_Walk_2.png")
        self.right_run_2_scaled = pygame.transform.scale(self.right_run_2, (65, 60))
        self.speed = 3
        self.last_pressed = True
        self.time = 0
        self.time_delayer = 0
        self.one_or_two = 0

    def draw(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_RIGHT]:
            self.walk_right()
            return
        if pressed_keys[pygame.K_LEFT]:
            self.walk_left()
            return
        if pressed_keys[pygame.K_UP]:
            if self.last_pressed == True:
                self.walk_right()
                return
            else:
                self.walk_left()
                return
        if pressed_keys[pygame.K_DOWN]:
            if self.last_pressed == True:
                self.walk_right()
                return
            else:
                self.walk_left()
                return
        else:
            if self.last_pressed == True:
                self.screen.blit(self.standing_right_1_scaled, (self.x, self.y))
            else:
                self.screen.blit(self.standing_left_1_scaled, (self.x, self.y))

    def walk_right(self):
        if self.time_delayer % 5 == 0:
            self.time = self.time + 1
        if self.time % 2 == 0:
            if self.one_or_two % 2 == 0:
                self.screen.blit(self.right_run_2_scaled, (self.x, self.y))
            else:
                self.screen.blit(self.right_run_1_scaled, (self.x, self.y))
        else:
            self.screen.blit(self.standing_right_1_scaled, (self.x, self.y))
            self.one_or_two = self.one_or_two + 1
        self.time_delayer = self.time_delayer + 1
        self.last_pressed = True

    def walk_left(self):
        if self.time_delayer % 5 == 0:
            self.time = self.time + 1
        if self.time % 2 == 0:
            if self.one_or_two % 2 == 0:
                self.screen.blit(self.left_run_2_scaled, (self.x, self.y))
            else:
                self.screen.blit(self.left_run_1_scaled, (self.x, self.y))
        else:
            self.screen.blit(self.standing_left_1_scaled, (self.x, self.y))
            self.one_or_two = self.one_or_two + 1
        self.time_delayer = self.time_delayer + 1
        print("Your mom gay")
        self.last_pressed = False
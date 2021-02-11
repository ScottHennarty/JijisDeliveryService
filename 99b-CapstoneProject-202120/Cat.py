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
        self.speed = 3
        self.last_pressed = True
        self.time = 0
        self.time_delayer = 0
        self.one_or_two = 0
        self.images()

    def images(self):
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

        self.forward_1 = pygame.image.load("New Gato/Cat_Forward_1.png")
        self.forward_1_scaled = pygame.transform.scale(self.forward_1, (60, 50))
        self.forward_2 = pygame.image.load("New Gato/Cat_Forward_2.png")
        self.forward_2_scaled = pygame.transform.scale(self.forward_2, (60, 50))
        self.forward_3 = pygame.image.load("New Gato/Cat_Forward_3.png")
        self.forward_3_scaled = pygame.transform.scale(self.forward_3, (60, 50))
        self.backward_1 = pygame.image.load("New Gato/Cat_Backwards_1.png")
        self.backward_1_scaled = pygame.transform.scale(self.backward_1, (60, 50))
        self.backward_2 = pygame.image.load("New Gato/Cat_Backwards_2.png")
        self.backward_2_scaled = pygame.transform.scale(self.backward_2, (60, 50))
        self.backward_3 = pygame.image.load("New Gato/Cat_Backwards_3.png")
        self.backward_3_scaled = pygame.transform.scale(self.backward_3, (60, 50))

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
            self.walk_forward()
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
        self.last_pressed = False

    def walk_forward(self):
        if self.time_delayer % 7 == 0:
            self.time = self.time + 1
        if self.time % 2 == 0:
            if self.one_or_two % 2 == 0:
                self.screen.blit(self.forward_2_scaled, (self.x, self.y))
            else:
                self.screen.blit(self.forward_3_scaled, (self.x, self.y))
        else:
            self.screen.blit(self.forward_1_scaled, (self.x, self.y))
            self.one_or_two = self.one_or_two + 1
            self.time_delayer = self.time_delayer + 1
            return
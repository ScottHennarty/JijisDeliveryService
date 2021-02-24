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
        self.time = 0
        self.time_delayer = 0
        self.one_or_two = 0
        self.radius = 200
        self.speed = 1.5
        self.speed_reset()
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        self.images()
        self.width = 70
        self.height = 65
        self.bark = 0

    def speed_reset(self):
        self.speed_right = self.speed
        self.speed_left = self.speed
        self.speed_up = self.speed
        self.speed_down = self.speed

    def images(self):
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
        self.forward_1 = pygame.image.load("New Perro/Dog_Forward_1.png")
        self.forward_1_scaled = pygame.transform.scale(self.forward_1, (60, 50))
        self.forward_2 = pygame.image.load("New Perro/Dog_Forward_2.png")
        self.forward_2_scaled = pygame.transform.scale(self.forward_2, (60, 50))
        self.forward_3 = pygame.image.load("New Perro/Dog_Forward_3.png")
        self.forward_3_scaled = pygame.transform.scale(self.forward_3, (60, 50))
        self.backward_1 = pygame.image.load("New Perro/Dog_Backward_1.png")
        self.backward_1_scaled = pygame.transform.scale(self.backward_1, (60, 50))
        self.backward_2 = pygame.image.load("New Perro/Dog_Backward_2.png")
        self.backward_2_scaled = pygame.transform.scale(self.backward_2, (60, 50))
        self.backward_3 = pygame.image.load("New Perro/Dog_Backward_3.png")
        self.backward_3_scaled = pygame.transform.scale(self.backward_3, (60, 50))
        self.bark_sound = pygame.mixer.Sound("Sounds/Dog Bark.wav")


    def draw(self, cat):
        if self.magnitude <= self.radius:
            if cat.x - self.x > 30:
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
            elif cat.x - self.x <= -30:
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
            else:
                if cat.y - self.y > 0:
                    if self.time_delayer % 11 == 0:
                        self.time = self.time + 1
                    if self.time % 2 == 0:
                        if self.one_or_two % 2 == 0:
                            self.screen.blit(self.forward_3_scaled, (self.x, self.y))
                        else:
                            self.screen.blit(self.forward_2_scaled, (self.x, self.y))
                    else:
                        self.screen.blit(self.forward_1_scaled, (self.x, self.y))
                        self.one_or_two = self.one_or_two + 1
                    self.time_delayer = self.time_delayer + 1
                else:
                    if self.time_delayer % 11 == 0:
                        self.time = self.time + 1
                    if self.time % 2 == 0:
                        if self.one_or_two % 2 == 0:
                            self.screen.blit(self.backward_3_scaled, (self.x, self.y))
                        else:
                            self.screen.blit(self.backward_2_scaled, (self.x, self.y))
                    else:
                        self.screen.blit(self.backward_1_scaled, (self.x, self.y))
                        self.one_or_two = self.one_or_two + 1
                    self.time_delayer = self.time_delayer + 1
            return
        else:
            if cat.x - self.x > 0:
                self.screen.blit(self.standing_right_1_scaled, (self.x, self.y))
            else:
                self.screen.blit(self.standing_left_1_scaled, (self.x, self.y))




    def move(self, cat):
        distance_x = cat.x - self.x
        distance_y = cat.y - self.y
        self.magnitude = math.sqrt(distance_x ** 2 + distance_y ** 2)
        if self.magnitude <= self.radius:
            if distance_x > -5:
                self.x = self.x + self.speed_right
            if distance_x < 5:
                self.x = self.x - self.speed_left
            if distance_y > -5:
                self.y = self.y + self.speed_down
            if distance_y < 5:
                self.y = self.y - self.speed_up
            self.bark = self.bark + 1
            if self.bark == 1:
                self.bark = 2
                self.bark_sound.play()
        else:
            self.bark = 0







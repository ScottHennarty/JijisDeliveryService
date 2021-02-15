import pygame
import sys
import time
import math



class Cat:
    def __init__(self, screen, true_screen):
        """ The cat sets the speed and is place in the center of the screen """
        self.screen = screen
        self.true_screen = true_screen
        self.x = (self.screen.get_width() - 100) // 2 + 100
        self.y = (self.screen.get_height() - 100) // 2 + 100
        self.speed = 3
        self.speed_reset()
        self.last_pressed = True
        self.time = 0
        self.time_delayer = 0
        self.one_or_two = 0
        self.images_sounds()
        self.height = 60
        self.width = 65

    def speed_reset(self):
        self.speed_right = 0
        self.speed_left = 0
        self.speed_up = 0
        self.speed_down = 0

    def images_sounds(self):
        self.standing_left_1 = pygame.image.load("New Gato/Cat_Left_Idle_1.png")
        self.standing_left_1_scaled = pygame.transform.scale(self.standing_left_1, (65, 60))
        self.standing_right_1 = pygame.image.load("New Gato/Cat_Right_Idle_1.png")
        self.standing_right_1_scaled = pygame.transform.scale(self.standing_right_1, (65, 60))
        self.left_run_1 = pygame.image.load("New Gato/Cat_Left_Walk_1.png")
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
        self.game_over =  pygame.image.load("Game Over.jpg")
        self.game_over_scaled = pygame.transform.scale(self.game_over, (1000, 800))
        self.game_over_sound = pygame.mixer.Sound("Sounds/Undertale Game Over Theme.wav")

    def draw(self):
        pressed_keys = pygame.key.get_pressed()
        # print(self.x, self.y)
        if pressed_keys[pygame.K_RIGHT]:
            self.walk_right()
            self.last_pressed = "Right"
            return
        if pressed_keys[pygame.K_LEFT]:
            self.walk_left()
            self.last_pressed = "Left"
            return
        if pressed_keys[pygame.K_UP]:
            self.walk_backward()
            self.last_pressed = "Up"
            return
        if pressed_keys[pygame.K_DOWN]:
            self.walk_forward()
            self.last_pressed = "Down"
            return
        else:
            if self.last_pressed == "Right":
                self.screen.blit(self.standing_right_1_scaled, (self.x, self.y))
                return
            if self.last_pressed == "Left":
                self.screen.blit(self.standing_left_1_scaled, (self.x, self.y))
                return
            if self.last_pressed == "Up":
                self.screen.blit(self.backward_1_scaled, (self.x, self.y))
                return
            else:
                self.screen.blit(self.forward_1_scaled, (self.x, self.y))

    def walk_right(self):
        if self.time_delayer % 7 == 0:
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
        if self.time_delayer % 7 == 0:
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

    def walk_backward(self):
        if self.time_delayer % 7 == 0:
            self.time = self.time + 1
        if self.time % 2 == 0:
            if self.one_or_two % 2 == 0:
                self.screen.blit(self.backward_2_scaled, (self.x, self.y))
            else:
                self.screen.blit(self.backward_3_scaled, (self.x, self.y))
        else:
            self.screen.blit(self.backward_1_scaled, (self.x, self.y))
            self.one_or_two = self.one_or_two + 1
        self.time_delayer = self.time_delayer + 1

    def move(self, camera_pos):
        print(self.x, self.y)
        pos_x, pos_y = camera_pos

        self.x += self.speed_right
        pos_x -= self.speed_right
        self.x -= self.speed_left
        pos_x += self.speed_left

        self.y -= self.speed_up
        pos_y += self.speed_up
        self.y += self.speed_down
        pos_y -= self.speed_down

        # if self.x < 0:
        #     self.x = 0
        #     pos_x = camera_pos[0]
        # elif self.x > 984:
        #     self.x = 984
        #     pos_x = camera_pos[0]
        # if self.y < 0:
        #     self.y = 0
        #     pos_y = camera_pos[1]
        # elif self.y > 984:
        #     self.y = 984
        #     pos_y = camera_pos[1]
        return (pos_x, pos_y)

    def lose(self):
        self.game_over_sound.play()
        return True






import pygame
import sys
import time
import math
from Cat import *
from Dog import *
from Walls import *

def main():
    pygame.init()
    pygame.display.set_caption("Jiji's Delivery Service ")
    screen = pygame.display.set_mode((1000, 600))

    cat = Cat(screen)
    wall = Walls(screen, 200, 200, 100, 200, (0, 255, 255), cat.speed)
    dog = Dog(screen, 900, 0)

    clock = pygame.time.Clock()
    while True:
        screen.fill((255, 255, 255))
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #The function here will set the cat speed depending on if the cat is
        #hitting a wall
        if wall.x + wall.width > wall.screen_width // 2 - 50 and wall.y + (
                    wall.height) > wall.screen_height // 2 - 40 and wall.y + (
                    0) < wall.screen_height // 2 + 1 and wall.x < wall.screen_width // 2:
            wall.x_speed_right = 0
            cat.speed_left = 0
        if wall.x < wall.screen_width // 2 + 10 and wall.y + (
                    wall.height) > wall.screen_height // 2 - 40 and wall.y + (
                    0) < wall.screen_height // 2 + 1 and wall.x + wall.width // 2 > wall.screen_width // 2:
            wall.x_speed_left = 0
            cat.speed_right = 0


        """This block should be for the Dog's movement"""
        dog.move()
        wall.move()

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_RIGHT]:
            dog.x = dog.x - cat.speed_right
        if pressed_keys[pygame.K_LEFT]:
            dog.x = dog.x + cat.speed_left
        if pressed_keys[pygame.K_UP]:
            dog.y = dog.y + cat.speed_up
        if pressed_keys[pygame.K_DOWN]:
            dog.y = dog.y - cat.speed_down

        dog.draw()
        wall.draw()
        cat.draw()


        #Reseting speed values
        wall.speed_reset()
        cat.speed_reset()

        pygame.display.update()


main()
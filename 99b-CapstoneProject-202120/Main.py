import pygame
import sys
import time
import math
import random
from Cat import *
from Dog import *
# from Walls import *

def main():
    pygame.init()
    pygame.display.set_caption("Jiji's Delivery Service ")
    screen = pygame.display.set_mode((1000, 600))

    dog = Dog(screen, random.randrange(50, 1000),random.randrange(200, 600))
    cat = Cat(screen)

    clock = pygame.time.Clock()
    while True:
        screen.fill((255, 255, 255))
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        """This block should be for the Dog's movement"""
        dog.move()

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_RIGHT]:
            dog.x = dog.x - cat.speed
        if pressed_keys[pygame.K_LEFT]:
            dog.x = dog.x + cat.speed
        if pressed_keys[pygame.K_UP]:
            dog.y = dog.y + cat.speed
        if pressed_keys[pygame.K_DOWN]:
            dog.y = dog.y - cat.speed
        if pressed_keys[pygame.K_SPACE]:
           main()

        dog.draw()
        cat.draw()

        pygame.display.update()





main()
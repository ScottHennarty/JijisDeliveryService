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
    screen = pygame.display.set_mode((1000, 800))
    clock = pygame.time.Clock()
    world = pygame.Surface((1000, 1000))

    cat = Cat(world)
    walls = [Walls(world, 200, 200, 100, 300, (88, 88, 88), cat.speed),
             Walls(world, 800, 200, 100, 200, (88, 88, 88), cat.speed)]

    dog = Dog(world, 700, 300)

    camera_pos = (0, 0)

    collision_offset = 5

    while True:
        world.fill((255, 255, 255))
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # The function here will set the cat speed depending on if the cat is
        # hitting a wall
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_RIGHT]:
            cat.speed_right = cat.speed
        if pressed_keys[pygame.K_LEFT]:
            cat.speed_left = cat.speed
        if pressed_keys[pygame.K_UP]:
            cat.speed_up = cat.speed
        if pressed_keys[pygame.K_DOWN]:
            cat.speed_down = cat.speed
        if pressed_keys[pygame.K_SPACE]:
            main()

        for wall in walls:
            # if wall.x + wall.width > wall.screen_width // 2 - 51 and wall.y + (
            #             wall.height) > wall.screen_height // 2 - 41 and wall.y + (
            #             0) < wall.screen_height // 2 and wall.x < wall.screen_width // 2:
            #     #wall.x_speed_right = 0
            #     cat.speed_left = 0
            # if wall.x < wall.screen_width // 2 + 10 and wall.y + (
            #             wall.height) > wall.screen_height // 2 - 39 and wall.y + (
            #             0) < wall.screen_height // 2 and wall.x + wall.width // 2 > wall.screen_width // 2:
            #     #wall.x_speed_left = 0
            #     cat.speed_right = 0
            # if wall.y + wall.height > wall.screen_height // 2 - 45 and wall.x + wall.width > wall.screen_width // 2 - 50 and wall.x < wall.screen_width // 2 and wall.y - 5 < wall.screen_height // 2 + 1:
            #     #wall.y_speed_down = 0
            #     cat.speed_down = 0
            # if wall.y + wall.height > wall.screen_height // 2 - 50 and wall.x + wall.width > wall.screen_width // 2 - 50 and wall.x < wall.screen_width // 2 and wall.y < wall.screen_height // 2:
            #     #wall.y_speed_up = 0
            #     cat.speed_up = 0
            if cat.y + cat.height > wall.y and cat.y + cat.height // 2 <= wall.y + wall.height:
                if wall.x < cat.x + collision_offset and wall.x + wall.width >= cat.x - collision_offset:
                    # wall.x_speed_right = 0
                    cat.speed_left = 0
                if wall.x + wall.width > cat.x - collision_offset and wall.x < cat.x + cat.width + collision_offset:
                    # wall.x_speed_left = 0
                    cat.speed_right = 0

            if cat.x + cat.width >= wall.x and cat.x <= wall.x + wall.width:
                if cat.y + cat.height + collision_offset >= wall.y:
                    # wall.y_speed_down = 0
                    cat.speed_down = 0
                if wall.y + wall.height >= cat.y - collision_offset:
                    # wall.y_speed_up = 0
                    cat.speed_up = 0

            if dog.y + dog.height > wall.y and dog.y + dog.height // 2 <= wall.y + wall.height:
                if wall.x < dog.x + collision_offset and wall.x + wall.width >= dog.x - collision_offset:
                    # wall.x_speed_right = 0
                    dog.speed_left = 0
                if wall.x + wall.width > dog.x - collision_offset and wall.x < dog.x + dog.width + collision_offset:
                    # wall.x_speed_left = 0
                    dog.speed_right = 0

            if dog.x + dog.width >= wall.x and dog.x <= wall.x + wall.width:
                if dog.y + dog.height + collision_offset >= wall.y:
                    # wall.y_speed_down = 0
                    dog.speed_down = 0
                if wall.y + wall.height >= dog.y - collision_offset:
                    # wall.y_speed_up = 0
                    dog.speed_up = 0
            """This block should be for the Dog's movement"""
            wall.draw()

        dog.move(cat)
        camera_pos = cat.move(camera_pos)
        # wall.move()

        # pressed_keys = pygame.key.get_pressed()
        # if pressed_keys[pygame.K_RIGHT]:
        #     dog.x = dog.x - cat.speed_right
        # if pressed_keys[pygame.K_LEFT]:
        #     dog.x = dog.x + cat.speed_left
        # if pressed_keys[pygame.K_UP]:
        #     dog.y = dog.y + cat.speed_up
        # if pressed_keys[pygame.K_DOWN]:
        #     dog.y = dog.y - cat.speed_down
        # if pressed_keys[pygame.K_SPACE]:
        #     main()

        dog.draw()
        cat.draw()

        # Reseting speed values
        # wall.speed_reset()
        # pygame.display.update()
        cat.speed_reset()
        dog.speed_reset()

        screen.blit(world, camera_pos)

        pygame.display.flip()


main()
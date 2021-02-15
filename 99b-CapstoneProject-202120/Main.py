import pygame
import sys
import time
import math
from Cat import *
from Dog import *
from Walls import *
from Keys import *

def main():
    pygame.init()
    pygame.display.set_caption("Jiji's Delivery Service ")
    screen = pygame.display.set_mode((1000, 800))
    clock = pygame.time.Clock()
    world = pygame.Surface((1000, 1000))

    cat = Cat(world)
    dog = Dog(world, 700, 200)
    walls = [Walls(world, 200, 200, 100, 300, (88, 88, 88), cat.speed),
             Walls(world, 800, 200, 100, 200, (88, 88, 88), cat.speed)]
    keys = [Keys(world, 400, 450, "Keys/Key_1.png", cat.speed),
            Keys(world, 500, 450, "Keys/Key_2.png", cat.speed),
            Keys(world, 600, 450, "Keys/Key_3.png", cat.speed)]

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


        #If I'm correct this is reponsible for stopping the wall if we walk into it
        for wall in walls:
            if cat.y + cat.height > wall.y and cat.y + cat.height // 2 <= wall.y + wall.height:
                if wall.x < cat.x + collision_offset and wall.x + wall.width >= cat.x - collision_offset:
                    cat.speed_left = 0
                if wall.x + wall.width > cat.x - collision_offset and wall.x < cat.x + cat.width + collision_offset:
                    cat.speed_right = 0

            if cat.x + cat.width >= wall.x and cat.x <= wall.x + wall.width:
                if cat.y + cat.height + collision_offset >= wall.y and cat.y + 15 * collision_offset < wall.y + wall.height:
                    cat.speed_down = 0
                if wall.y + wall.height >= cat.y - collision_offset and wall.y < cat.y + cat.height:
                    cat.speed_up = 0

            if dog.y + dog.height > wall.y and dog.y + dog.height // 2 <= wall.y + wall.height:
                if wall.x < dog.x + collision_offset and wall.x + wall.width >= dog.x - collision_offset:
                    dog.speed_left = 0
                if wall.x + wall.width > dog.x - collision_offset and wall.x < dog.x + dog.width + collision_offset:
                    dog.speed_right = 0

            if dog.x + dog.width >= wall.x and dog.x <= wall.x + wall.width:
                if dog.y + dog.height + collision_offset >= wall.y and dog.y + 15 * collision_offset < wall.y + wall.height:
                    dog.speed_down = 0
                if wall.y + wall.height >= dog.y - collision_offset and wall.y < dog.y + cat.height:
                    dog.speed_up = 0
            wall.draw()

        #This will draw keys
        counter = 0
        for key in keys:
            key.draw()
            current = key.collect_key(cat)
            if current == 1:
                counter = counter + 1
                if counter == 3:
                    key.catch_em_all(dog)

        dog.move(cat)
        camera_pos = cat.move(camera_pos)

        dog.draw(cat)
        cat.draw()

        # Reseting speed values
        # pygame.display.update()
        cat.speed_reset()
        dog.speed_reset()

        screen.blit(world, camera_pos)

        pygame.display.flip()


main()

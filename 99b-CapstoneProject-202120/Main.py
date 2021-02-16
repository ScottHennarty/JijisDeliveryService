import pygame
import sys
import time
import math
from Cat import *
from Dog import *
from Walls import *
from Keys import *
from Stamina_Bar import *
from Fish import *
from Positions import *

def main():
    pygame.init()
    pygame.display.set_caption("Jiji's Delivery Service ")
    screen = pygame.display.set_mode((1000, 800))
    clock = pygame.time.Clock()
    world = pygame.Surface((2500, 2500))
    game_over = False
    screen_offset = 500
    walking_space = 100

    cat = Cat(world, screen)
    positions = Positions(world, screen, screen_offset, walking_space, cat)
    dogs = positions.dogs
    for dog in dogs:
        dog.speed_reset()
    #(x,y,width,height,(color))
    walls = positions.walls
    keys = positions.keys
    fishes = positions.fishes
    stamina = Stamina(screen, 400, 40, 5)

    camera_pos = (-cat.x + (screen.get_width() // 2), -cat.y + (screen.get_height() // 2))

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
            if cat.y + cat.height >= wall.y and cat.y + cat.height // 2 <= wall.y + wall.height:
                if wall.x < cat.x + collision_offset and wall.x + wall.width > cat.x - collision_offset:
                    cat.speed_left = 0
                elif wall.x + wall.width > cat.x - collision_offset and wall.x < cat.x + cat.width + collision_offset:
                    cat.speed_right = 0

            elif cat.x + cat.width >= wall.x and cat.x <= wall.x + wall.width:
                if cat.y + cat.height + collision_offset > wall.y and cat.y + 15 * collision_offset < wall.y + wall.height:
                    cat.speed_down = 0
                elif wall.y + wall.height > cat.y - collision_offset and wall.y < cat.y + cat.height:
                    cat.speed_up = 0


            for dog in dogs:
                if dog.y + dog.height >= wall.y and dog.y + dog.height // 2 <= wall.y + wall.height:
                    if wall.x < dog.x + collision_offset and wall.x + wall.width > dog.x - collision_offset:
                        dog.speed_left = 0
                    elif wall.x + wall.width > dog.x - collision_offset and wall.x < dog.x + dog.width + collision_offset:
                        dog.speed_right = 0

                elif dog.x + dog.width >= wall.x and dog.x <= wall.x + wall.width:
                    if dog.y + dog.height + collision_offset > wall.y and dog.y + 15 * collision_offset < wall.y + wall.height:
                        dog.speed_down = 0
                    elif wall.y + wall.height > dog.y - collision_offset and wall.y < dog.y + cat.height:
                        dog.speed_up = 0
            wall.draw()

        for fish in fishes:
            fish.eat_fish(stamina, cat)
            fish.draw()

        for dog in dogs:
            dog.move(cat)
            dog.draw(cat)

        #This will draw keys
        counter = 0
        for key in keys:
            key.draw()
            current = key.collect_key(cat)
            if current == 1:
                counter = counter + 1
                if counter == 3:
                    key.catch_em_all(dogs)

        camera_pos = cat.move(camera_pos)
        cat.draw()
        stamina.drain()

        # Reseting speed values
        # pygame.display.update()
        cat.speed_reset()
        dog.speed_reset()

        screen.blit(world, camera_pos)
        stamina.draw()

        # This checks to see if the player has lost
        for dog in dogs:
            magnitude = math.sqrt((cat.x - dog.x) ** 2 + (cat.y - dog.y) ** 2)
            if magnitude <= 40:
                game_over = cat.lose()
            if game_over == True:
                screen.blit(cat.game_over_scaled, (0, 0))
            game_over = stamina.game_over(cat)
            if game_over == True:
                screen.blit(cat.game_over_scaled, (0, 0))
        pygame.display.flip()



main()

import pygame
import sys
import time
import math
import random
import copy
from Cat import *
from Dog import *
from Walls import *
from Keys import *
from Stamina_Bar import *
from Fish import *
# from Main import *
#screen, x, y, width, height, color, speed
class Positions:
    def __init__(self, world, screen, screen_offset, walking_space, cat, regen, dog_num, fish_num):
        self.world = world
        self.regen = regen
        self.walls = [Walls(world, screen_offset, screen_offset, 50, world.get_height() - 2 * screen_offset, (88, 88, 88), cat.speed),
             Walls(world, screen_offset, screen_offset, world.get_width() - 2 * screen_offset, 50, (88, 88, 88), cat.speed),
             Walls(world, world.get_width() - screen_offset, screen_offset, 50, world.get_height() - 2 * screen_offset + 50, (88, 88, 88), cat.speed),
             Walls(world, screen_offset, world.get_width() - screen_offset, world.get_width() - 2 * screen_offset, 50, (88, 88, 88), cat.speed),
             Walls(world, 1100, 1000, 400, 50, (88, 88, 88), cat.speed), Walls(world, 1100, 1000, 50, 200, (88, 88, 88), cat.speed),
             Walls(world, 1450, 1000, 50, 200, (88, 88, 88), cat.speed), Walls(world, 900, 1350, 800, 50, (88, 88, 88), cat.speed),
             Walls(world, 1100, 800, 400, 50, (88, 88, 88), cat.speed), Walls(world, 900, 900, 50, 300, (88, 88, 88), cat.speed),
             Walls(world, 1650, 900, 50, 300, (88, 88, 88), cat.speed), Walls(world, 700, 700, 50, 200, (88, 88, 88), cat.speed),
             Walls(world, 700, 700, 200, 50, (88, 88, 88), cat.speed), Walls(world, 1650, 700, 200, 50, (88, 88, 88), cat.speed),
             Walls(world, 1800, 700, 50, 200, (88, 88, 88), cat.speed), Walls(world, 1150, 500, 50, 150, (88, 88, 88), cat.speed),
             Walls(world, 1400, 500, 50, 150, (88, 88, 88), cat.speed), Walls(world, 1800, 1000, 200, 50, (88, 88, 88), cat.speed),
             Walls(world, 1800, 1000, 50, 400, (88, 88, 88), cat.speed), Walls(world, screen_offset, 1000, 200, 50, (88, 88, 88), cat.speed),
             Walls(world, 700, 1000, 50, 400, (88, 88, 88), cat.speed), Walls(world, 1175, 1550, 50, 200, (88, 88, 88), cat.speed),
             Walls(world, 1375, 1550, 50, 200, (88, 88, 88), cat.speed), #I can't be bothered to fix this sorry!
             Walls(world, 1375, 1700, 175, 50, (88, 88, 88), cat.speed), Walls(world, 1050, 1700, 150, 50, (88, 88, 88), cat.speed),
             Walls(world, 900, 1550, 50, 200, (88, 88, 88), cat.speed), Walls(world, 1650, 1550, 50, 200, (88, 88, 88), cat.speed),
             Walls(world, 900, 1550, 175, 50, (88, 88, 88), cat.speed), Walls(world, 1525, 1550, 150, 50, (88, 88, 88), cat.speed),
             Walls(world, 1800, 1550, 50, 350, (88, 88, 88), cat.speed), Walls(world, 1800, 1550, 50, 350, (88, 88, 88), cat.speed),
             Walls(world, 700, 1550, 50, 350, (88, 88, 88), cat.speed), Walls(world, 1075, 1850, 450, 50, (88, 88, 88), cat.speed),
             Walls(world, 750, 1850, 200, 50, (88, 88, 88), cat.speed), Walls(world, 1650, 1850, 200, 50, (88, 88, 88), cat.speed)]
        #This one will create a list of dog based on how many we want
        self.dogs = []
        self.dog_positions_ref = [Dog(world, 1550, 900), Dog(world, 1000, 900), Dog(world, 800, 1450), Dog(world, 1700, 1450),
                     Dog(world, 1900, 750), Dog(world, 600, 750), Dog(world, 1275, 700), Dog(world, 600, 1875), Dog(world, 1900, 1875),
                     Dog(world, 1275, 1600), Dog(world, 1450, 1900), Dog(world, 1075, 1900), Dog(world, 775, 1075), Dog(world, 1725, 1075)]
        self.dog_positions = [Dog(world, 1550, 900), Dog(world, 1000, 900), Dog(world, 800, 1450), Dog(world, 1700, 1450),
                     Dog(world, 1900, 750), Dog(world, 600, 750), Dog(world, 1275, 700), Dog(world, 600, 1875), Dog(world, 1900, 1875),
                     Dog(world, 1275, 1600), Dog(world, 1450, 1900), Dog(world, 1075, 1900), Dog(world, 775, 1075), Dog(world, 1725, 1075)]
        for d in range(dog_num):
            dog_passed = False
            while dog_passed == False:
                dog_place = random.randint(0, len(self.dog_positions) - 1)
                if self.dog_positions[dog_place].x != 0:
                    dog_passed = True
                    self.dog_positions[dog_place].x = 0
            self.dogs = self.dogs + [self.dog_positions_ref[dog_place]]
        #displays all dogs
            # self.dogs = [Dog(world, 1550, 900), Dog(world, 1000, 900), Dog(world, 800, 1450), Dog(world, 1700, 1450),
            #          Dog(world, 1900, 750), Dog(world, 600, 750), Dog(world, 1275, 700), Dog(world, 600, 1875), Dog(world, 1900, 1875),
            #          Dog(world, 1275, 1600), Dog(world, 1450, 1900), Dog(world, 1075, 1900), Dog(world, 775, 1075), Dog(world, 1725, 1075)]


        self.keys = [Keys(world, 0, 0, "Keys/Key_1.png", cat.speed),
            Keys(world, 0, 0, "Keys/Key_2.png", cat.speed),
            Keys(world, 0, 0, "Keys/Key_3.png", cat.speed)]
        self.key_position_x_ref = [600, 1900, 1500, 1000, 1275, 600, 1900]
        self.key_position_y_ref = [1100, 1100, 1625, 1625, 575, 600, 600]
        self.key_available = [1, 1, 1, 1, 1, 1, 1]
        for k in range(3):
            key_passed = False
            while key_passed == False:
                key_place = random.randint(0, len(self.key_available) - 1)
                if self.key_available[key_place] != 0:
                    key_passed = True
                    self.key_available[key_place] = 0
            self.keys[k].x = self.key_position_x_ref[key_place]
            self.keys[k].y = self.key_position_y_ref[key_place]

        self.fishes = []
        self.fish_position_x_ref = [1650, 900, 600, 1900, 1275, 800, 1700, 1275, 1275, 800, 1725, 1550, 1000]
        self.fish_position_y_ref = [1250, 1250, 1450, 1450, 900, 800, 800, 1450, 1775, 1650, 1650, 1925, 1925]
        self.fish_available = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        for f in range(fish_num):
            fish_passed = False
            while fish_passed == False:
                fish_place = random.randint(0, len(self.fish_available) - 1)
                if self.fish_available[fish_place] != 0:
                    fish_passed = True
                    self.fish_available[fish_place] = 0
            self.fishes = self.fishes + [Fishes(world, self.fish_position_x_ref[fish_place], self.fish_position_y_ref[fish_place], self.regen)]
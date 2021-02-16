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
# from Main import *
#screen, x, y, width, height, color, speed
class Positions:
    def __init__(self, world, screen, screen_offset, walking_space, cat, regen):
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
        self.dogs = [Dog(world, 0, 0), Dog(world, 1550, 900), Dog(world, 1275, 1600), Dog(world, 1700, 1925), Dog(world, 800, 800), Dog(world, 800, 1500),
        Dog(world, 1275, 700)]
        self.keys = [Keys(world, 1275, 575, "Keys/Key_1.png", cat.speed),
            Keys(world, 600, 1100, "Keys/Key_2.png", cat.speed),
            Keys(world, 1500, 1625, "Keys/Key_3.png", cat.speed)]
        self.fishes = [Fishes(world, 1675, 1250, self.regen), Fishes(world, 1900, 600, self.regen),
              Fishes(world, 1275, 900, self.regen), Fishes(world, 1700, 1775, self.regen), Fishes(world, 1000, 1925, self.regen),
              Fishes(world, 800, 1650, self.regen)]
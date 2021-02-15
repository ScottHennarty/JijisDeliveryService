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

class Positions:
    def __init__(self, world, screen, screen_offset, walking_space, cat):
        self.walls = [Walls(world, screen_offset, screen_offset, 100, world.get_height() - 2 * screen_offset, (88, 88, 88), cat.speed),
             Walls(world, screen_offset, screen_offset, world.get_width() - 2 * screen_offset, 100, (88, 88, 88), cat.speed),
             Walls(world, world.get_width() - screen_offset, screen_offset, 100, world.get_height() - 2 * screen_offset + 100, (88, 88, 88), cat.speed),
             Walls(world, screen_offset, world.get_width() - screen_offset, world.get_width() - 2 * screen_offset, 100, (88, 88, 88), cat.speed)]
        self.dogs = [Dog(world, 700, 200), Dog(world, 700, 50)]
        self.keys = [Keys(world, 400, 450, "Keys/Key_1.png", cat.speed),
            Keys(world, 500, 450, "Keys/Key_2.png", cat.speed),
            Keys(world, 600, 450, "Keys/Key_3.png", cat.speed)]
        self.fishes = [Fishes(world, 250, 450, 20), Fishes(world, 250, 500, 20),
              Fishes(world, 250, 550, 20), Fishes(world, 250, 600, 20)]
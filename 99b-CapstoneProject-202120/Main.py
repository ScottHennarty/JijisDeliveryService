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
        self.standing_image = pygame.image.load("Definetly_A_Dog.png")
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        self.radius = 400

    def draw(self):
        self.screen.blit(self.standing_image, (self.x, self.y))

    def move(self):
        distance_x = (self.screen_width // 2) - self.x
        distance_y = (self.screen_height // 2) - self.y
        magnitude = math.sqrt(distance_x ** 2 + distance_y ** 2)
        if magnitude <= self.radius:
            if distance_x > 0:
                self.x = self.x + 2
            if distance_x < 0:
                self.x = self.x - 2
            if distance_y > 0:
                self.y = self.y + 2
            if distance_y < 0:
                self.y = self.y - 2

class Cat:
    def __init__(self, screen):
        """ The cat sets the speed and is place in the center of the screen """
        self.screen = screen
        self.x = self.screen.get_width() // 2 - 50
        self.y = self.screen.get_height() // 2 - 50
        self.standing_image = pygame.image.load("Cute_Kitten.png")
        self.speed = 3

    def draw(self):
        self.screen.blit(self.standing_image, (self.x, self.y))



def main():
    pygame.init()
    pygame.display.set_caption("Jiji's Delivery Service ")
    screen = pygame.display.set_mode((1000, 600))

    dog = Dog(screen, 0, 0)
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

        dog.draw()
        cat.draw()

        pygame.display.update()





main()
import pygame
import random

class Duck:
    def __init__(self):
        self.load = pygame.image.load("assets/duck.png")
        self.duck_width = 50
        self.duck_height = 50
        self.scale = pygame.transform.scale(self.load, (self.duck_width, self.duck_height))
        self.entities = []
        self.coordinates = [random.randint(0, 1230), random.randint(0, 550)]
        self.move_coordinates = [random.randint(0, 1230), random.randint(0, 550)]
        self.scale.convert()
        self.speed = 0.5

    def ducks_generator(self, amount):
        for i in range(amount):
            self.entities.append(Duck())


    def render_duck(self, display):
        #if (self.coordinates[0] - 10) > 0 and (self.coordinates[0] + 10) + self.duck_width < 1280:
        if self.coordinates[0] < self.move_coordinates[0] and self.coordinates[0] != self.move_coordinates[0]:
            self.coordinates[0] += self.speed
        elif self.coordinates[0] > self.move_coordinates[0] and self.coordinates[0] != self.move_coordinates[0]:
            self.coordinates[0] -= self.speed
        else:
            self.move_coordinates = [random.randint(0, 1230), random.randint(0, 550)]

        if self.coordinates[1] < self.move_coordinates[1] and self.coordinates[1] != self.move_coordinates[1]:
            self.coordinates[1] += self.speed
        elif self.coordinates[1] > self.move_coordinates[1] and self.coordinates[1] != self.move_coordinates[1]:
            self.coordinates[1] -= self.speed
        else:
            self.move_coordinates = [random.randint(0, 1230), random.randint(0, 550)]
        #else:
            #self.move_coordinates = [random.randint(0, 1230), random.randint(0, 550)]
            # if self.move_coordinates[0] > self.coordinates[0]:
            #   self.coordinates[0] += 0.1

            # print(self.move_coordinates)

        display.blit(self.scale, (self.coordinates[0], self.coordinates[1]))

    def delete_duck(self, mouse_position, duck, position):
        if self.coordinates[0] <= mouse_position[0] <= (self.coordinates[0] + self.duck_width) \
                and self.coordinates[1] <= mouse_position[1] <= self.coordinates[1] + self.duck_height:
            duck.entities.pop(position)
            pygame.display.update()

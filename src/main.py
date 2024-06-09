import pygame
import time
from Classes.Duck import Duck
from Classes.Dog import Dog
from Classes.Player import Player
from Classes.Menu import Menu


class Game:
    def __init__(self):

        pygame.init()

        #Screen settings
        self.WIDTH = 1280
        self.HEIGHT = 720
        self.FPS = 60
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.screen.fill((255, 255, 255))
        self.caption = pygame.display.set_caption("DuckHunt by DaNtR3")
        self.logo = pygame.image.load("Assets/icon.jpg")
        self.icon = pygame.display.set_icon(self.logo)
        self.bg = pygame.image.load("assets/img.png")
        self.bg.convert()
        self.clock = pygame.time.Clock()
        
        #----------------------------------------------------------------------
        
        #Instantiating classes
        self.player1 = Player()
        self.dog = Dog()
        self.duck = Duck()
        self.menu = Menu()
        #----------------------------------------------------------------------
    
    def game_a_loop(self):
        self.duck.ducks_generator(4)
            
        while True:
            # Character rendering
                # Screen settings            
            self.screen.fill((255, 255, 255))
            self.screen.blit(self.bg, (0, 0))
            for ducks in self.duck.entities:
                ducks.render_duck(self.screen)
            self.dog.render_dog(self.screen)
            self.player1.render_current_position(self.screen)
            # Screen update
            pygame.display.update()
            # Controls during the loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # for ducks in self.duck.entities:
                    # ducks.delete_duck(pygame.mouse.get_pos(), self.duck)
                    for list_position in range(len(self.duck.entities)):
                        if list_position == len(self.duck.entities):
                            self.duck.entities[list_position - 1].delete_duck(pygame.mouse.get_pos(), self.duck,
                                                                              list_position)
                        else:
                            self.duck.entities[list_position].delete_duck(pygame.mouse.get_pos(), self.duck, list_position)                   
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.player1.update_left_movements(self.screen)
                    elif event.key == pygame.K_d:
                        self.player1.update_right_movements(self.screen)
                   
                    
            
    def game_loop(self):

        pygame.time.set_timer(pygame.USEREVENT,0)
        
        # Screen refresh rate
        self.clock.tick(self.FPS)
        

        while True:
            self.menu.render_menu(self.screen, self.WIDTH, self.HEIGHT)
            # Controls during the loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.menu.move_cursor_down()
                    elif event.key == pygame.K_UP:
                        self.menu.move_cursor_up()
                    elif event.key == pygame.K_RETURN:
                        self.game_a_loop()

            # Screen update
            pygame.display.update()
            #time.sleep(0)
            # Test code
            # print(self.duck.entities)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Game().game_loop()

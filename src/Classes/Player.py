import pygame



class Player:
    def __init__(self):
        self.x = 600
        self.y = 600
        self.move = 10
        self.player_height = 80
        self.player_width = 80
        self.load = pygame.image.load("assets/player.png")
        self.scale = pygame.transform.flip(pygame.transform.scale(self.load, (self.player_width, self.player_height)),
                                           False, False)

    
    def render_current_position(self, display):
        display.blit(self.scale, (self.x, self.y))
    
    def update_left_movements(self, display):
        if self.x - self.move > 0:
            print(self.x)
            self.scale = pygame.transform.flip(
                pygame.transform.scale(self.load,(self.player_width, self.player_height)),
                True, False)
            self.x -= self.move
        #display.blit(self.scale, (self.x, self.y))    
   
    
    def update_right_movements(self, display):
        if (self.x + self.move) + self.player_width < 1280:
            print(self.x)
            self.scale = pygame.transform.flip(
                pygame.transform.scale(self.load, (self.player_width, self.player_height)),
                False, False)
            self.x += self.move

        #display.blit(self.scale, (self.x, self.y))    
        
        
#Backup
    '''def render_player_movements(self, keys_pressed, display):
        if keys_pressed[pygame.K_a] and (self.x - self.move) > 0:
            print(self.x)
            self.scale = pygame.transform.flip(
                pygame.transform.scale(self.load,(self.player_width, self.player_height)),
                True, False)
            self.x -= self.move

        if keys_pressed[pygame.K_d] and (self.x + self.move) + self.player_width < 1280:
            print(self.x)
            self.scale = pygame.transform.flip(
                pygame.transform.scale(self.load, (self.player_width, self.player_height)),
                False, False)
            self.x += self.move

        display.blit(self.scale, (self.x, self.y))'''



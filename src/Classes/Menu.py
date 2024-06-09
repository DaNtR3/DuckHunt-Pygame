
import pygame

class Menu:
    def __init__(self):
        
        self.main_border = None
        self.orange = (255, 153, 51)
        self.black = (0,0,0)
        self.light_blue = (11, 255, 232)
        self.white = (255, 255, 255)
        self.green = (0, 255, 0)
        self.line_start_pos = (175, 225)
        self.line_end_pos = (1090, 225)
        self.font_title_size = 155
        self.font_options_size = 35
        self.font_option_obj = pygame.font.SysFont('Duck Hunt', self.font_options_size)
        self.font_title_obj = pygame.font.SysFont('M29_DUCK HOUND', self.font_title_size)
        self.text_duck = self.font_title_obj.render('DUCK', False, self.light_blue)
        self.text_hunt = self.font_title_obj.render('HUNT', False, self.light_blue)
        self.text_game_a = self.font_option_obj.render('Game A', False, self.orange)
        self.text_game_b = self.font_option_obj.render('Game B', False, self.orange)
        self.text_game_c = self.font_option_obj.render('Game C', False, self.orange)
        self.text_1_duck = self.font_option_obj.render('1 Duck', False, self.orange)
        self.text_2_ducks = self.font_option_obj.render('2 Ducks', False, self.orange)
        self.text_clay_shooting = self.font_option_obj.render('Clay shooting', False, self.orange)
        self.text_top_score = self.font_option_obj.render('Top Score = 12000', False, self.green)
        self.text_author = self.font_option_obj.render('©2023 DaNtR3 CO..LTD.', False, self.white)
        self.cursor_coordinates_a = [(375, 460),(400, 460), (385, 440), (385, 450), (375, 450)]
        self.cursor_coordinates_b = [(375, 515),(400, 515), (385, 495), (385, 505), (375, 505)]
        self.cursor_coordinates_c = [(375, 570),(400, 570), (385, 550), (385, 560), (375, 560)]
        self.cursor_list = (self.cursor_coordinates_a,self.cursor_coordinates_b, self.cursor_coordinates_c )
        self.current_position = self.cursor_list[0]
       
        
        '''self.current_position_b = self.cursor_coordinates_a[(1)]
        self.current_position_c = self.cursor_coordinates_a[(1)]'''
        

    def render_menu(self, display, WIDTH, HEIGHT):
        
        self.main_border = pygame.Rect(0, 0, WIDTH, HEIGHT)
        pygame.draw.rect(display, self.black, self.main_border)
        pygame.draw.line(display, self.orange, self.line_start_pos, self.line_end_pos, 10)
        pygame.draw.polygon(display, self.white, self.current_position, 0), (30, 30)
        #self.current_position = self.times
                
        display.blit(self.text_duck, (175, 55))
        display.blit(self.text_hunt, (515, 235))
        display.blit(self.text_game_a, (415, 435))
        display.blit(self.text_game_b, (415, 490))
        display.blit(self.text_game_c, (415, 545))
        display.blit(self.text_1_duck, (790, 435))
        display.blit(self.text_2_ducks, (790, 490))
        display.blit(self.text_clay_shooting, (790, 545))
        display.blit(self.text_top_score, (540, 620))
        display.blit(self.text_author, (500, 675))
        
    def move_cursor_down(self): 
        if self.current_position == self.cursor_coordinates_a:
            self.current_position = self.cursor_coordinates_b
        elif self.current_position == self.cursor_coordinates_b:
            self.current_position = self.cursor_coordinates_c
        else:
            self.current_position = self.cursor_coordinates_a
    
    def move_cursor_up(self):
        if self.current_position == self.cursor_coordinates_a:
            self.current_position = self.cursor_coordinates_c
        elif self.current_position == self.cursor_coordinates_b:
            self.current_position = self.cursor_coordinates_a
        else:
            self.current_position = self.cursor_coordinates_b
               
        

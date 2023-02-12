
import pygame

class Menu:
    def __init__(self):
        
        self.main_border = None
        self.orange = (255, 153, 51)
        self.black = (0,0,0)
        self.light_blue = (11, 255, 232)
        self.green = (0, 255, 0)
        self.line_start_pos = (175, 225)
        self.line_end_pos = (1090, 225)
        self.font_title_size = 155
        self.font_options_size = 20
        self.font_option_obj = pygame.font.SysFont('M29_DUCK HOUND', self.font_options_size)
        self.font_title_obj = pygame.font.SysFont('M29_DUCK HOUND', self.font_title_size)
        self.text_duck = self.font_title_obj.render('DUCK', False, self.light_blue)
        self.text_hunt = self.font_title_obj.render('HUNT', False, self.light_blue)
        self.text_game_a = self.font_option_obj.render('Game A', False, self.orange)
        self.text_game_b = self.font_option_obj.render('Game B', False, self.orange)
        self.text_game_c = self.font_option_obj.render('Game C', False, self.orange)
        self.text_1_duck = self.font_option_obj.render('1 Duck', False, self.orange)
        self.text_2_ducks = self.font_option_obj.render('2 Ducks', False, self.orange)
        self.text_clay_shooting = self.font_option_obj.render('Clay shooting', False, self.orange)
        self.text_top_score = self.font_option_obj.render('Top Score: 12000', False, self.green)


    def render_menu(self, display, WIDTH, HEIGHT):
        self.main_border = pygame.Rect(0, 0, WIDTH, HEIGHT)
        pygame.draw.rect(display, self.black, self.main_border)
        pygame.draw.line(display, self.orange, self.line_start_pos, self.line_end_pos, 10)
        display.blit(self.text_duck, (175, 55))
        display.blit(self.text_hunt, (515, 235))
        display.blit(self.text_game_a, (415, 435))
        display.blit(self.text_game_b, (415, 490))
        display.blit(self.text_game_c, (415, 545))
        display.blit(self.text_1_duck, (715, 435))
        display.blit(self.text_2_ducks, (715, 490))
        display.blit(self.text_clay_shooting, (715, 545))
        display.blit(self.text_top_score, (540, 620))
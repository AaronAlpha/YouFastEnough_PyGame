import pygame

import FunctionsFile as func

class Buttons:
    def __init__(self, x, y, text, fontSize, w, h, color):
        self.x = x
        self.y = y
        self.textIMG = text
        self.fontSize = fontSize
        self.width = w
        self.height = h
        self.color = color
        
        self.clicked = False

    def draw(self, screen):
        action = False          
        pos = pygame.mouse.get_pos()
        button_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
        if button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                
                action = True
                self.clicked = True
                pygame.draw.rect(screen, (100, 100, 100), (button_rect))
            elif pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
                pygame.draw.rect(screen, (45, 185, 122), (button_rect))
        else:
            pygame.draw.rect(screen, self.color, (button_rect))
        
        textFont = pygame.font.Font("TechnoRaceItalic-eZRWe.otf", self.fontSize)
        font = pygame.font.SysFont(None, 30)
        textIMG = font.render(self.textIMG, True, (0, 0, 0))
        text_len = textIMG.get_width()

        func.draw_text(screen, self.textIMG, textFont, (0, 0, 0), button_rect.x + int(self.width/2) - int(text_len/2) - 20, button_rect.y + 10)
        
        return action

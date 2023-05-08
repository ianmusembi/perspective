# Photomanipulator
# Author : Ian Musembi


# button.py


'''
These buttons are to be used in the main menu
'''

import pygame

pygame.font.init()

# CONSTANTS
hovering_colour = (255, 255, 102)   # rgb for light shade of yellow
white = (255, 255, 255)
red = (255,0,0,255)
green = (0,255,0,255)
blue = (0,0,255,255)
black = (0, 0, 0, 255)
skyBlue = (0,191,255)
silver = (192,192,192)
grey = (128,128,128)

class Button():

    def __init__(self, pos, text, base_color, hovering_color = hovering_colour , image = None, font = None, fontSize = 30 ):
        self.image = image              #image is a pygame surface object
        self.x_pos = pos[0]             #pos is a tuple containing x and y coordinates
        self.y_pos = pos[1]  

        if font is not None:            
            self.font = font
        else:
            self.font = self.createFont(fontSize)
        
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text = text
        self.buttonText = self.font.render(self.text, True, self.base_color)

        if self.image is None:
            self.image = self.buttonText
            
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.buttonText_rect = self.buttonText.get_rect(center=(self.x_pos, self.y_pos))

    def draw(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        
        screen.blit(self.text, self.buttonText_rect)

    # def update(self, screen):
    #     if self.image is not None:
    #         screen.blit(self.image, self.rect)
    #     screen.blit(self.buttonText, self.buttonText_rect)


    def isClicked(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def showHoveringState(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text, True, self.base_color)

    @staticmethod
    def createFont(fontSize):
       
        List = pygame.font.get_fonts()

        # if fonts are found
        if (len(List) > 0):
            font = pygame.font.SysFont(List[1], fontSize)
            return font
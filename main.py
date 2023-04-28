
# Photomanipulator
# Author : Ian Musembi
# Version 1.0.0

# main.py

'''
Redraws images using pointilsm art technique
'''

import pygame
import sys

pygame.font.init()

from pointilismFunctions import *
from fileBrowser import * # selectImage
from button import *

pygame.font.init()

# CONSTANTS
red = (255,0,0,255)
green = (0,255,0,255)
blue = (0,0,255,255)
white = (255,255,255,255)
black = (0, 0, 0, 255)
skyBlue = (0,191,255)

SCREEN = pygame.display.set_mode((1280,720))
BACKGROUND_IMAGE = "images/homescreen2.png"


def main_menu(screen):
    
    background_img = pygame.image.load(BACKGROUND_IMAGE)
    

    while True:
        pygame.display.set_caption("Menu")
        
        screen.blit(background_img, (0,0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        

        MENU_TEXT = Button.createFont(75).render("SELECT AN OPTION", True, black)
        MENU_RECT = MENU_TEXT.get_rect(center=(600,38))

        POINTILISM_BUTTON = Button(pos = (600, 200), text = "POINTILISM", base_color = white, 
                                   hovering_color = skyBlue,
                                   fontSize = 50)
        
        QUIT_BUTTON = Button(pos = (600, 400), text = "QUIT", base_color = white,
                            hovering_color = skyBlue,
                            fontSize = 50)
        
        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [POINTILISM_BUTTON, QUIT_BUTTON] :
            button.showHoveringState(MENU_MOUSE_POS)
            button.draw(screen)


        # EVENT HANDLERS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if POINTILISM_BUTTON.isClicked(MENU_MOUSE_POS):
                    filePath = selectImage()
                    pointilism(screen, filePath)
                
                if QUIT_BUTTON.isClicked(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

# ------------------END OF MAIN FUNCTION -----------------------------------

def pointilism(screen, path):

    screen.fill(black)
    alreadyDrawn = False

    while True:
        pygame.display.set_caption("Pointilism")
        
        
        

        POINTILISM_MOUSE_POS = pygame.mouse.get_pos()

        QUIT_BUTTON = Button(pos = (150, 600), text = "QUIT", base_color = white,
                                hovering_color = skyBlue,
                                #image = pygame.image.load("buttonRect.png"),
                                fontSize = 50)
        
        BACK_BUTTON = Button(pos = (180, 400), text = "MAIN MENU", base_color = white,
                                hovering_color = skyBlue,
                                #image = pygame.image.load("buttonRect.png"),
                                fontSize = 50)
        
        for button in [BACK_BUTTON, QUIT_BUTTON] :
            button.showHoveringState(POINTILISM_MOUSE_POS)
            button.draw(screen)


        if not alreadyDrawn :

            width, height = screen.get_size()

            # path = "makori.png" 

            src_img = pygame.image.load(path)
            resized_img = pygame.transform.scale(src_img, (300, 180))


            (src_width,src_height) = src_img.get_size()
            (resized_width, resized_height) = resized_img.get_size()


            #x and y scale factor of the pointilism image to the resized image
            width_factor = int((width - resized_width)/resized_width)
            height_factor = int(height/resized_height) 


            #display source image on top left corner of the screen
            screen.blit(resized_img, (0,0))

            pygame.display.update()
            pygame.time.delay(1000)

            #nested row and column loops to go through each pixel in the source image
            for row in range(src_height):
                for col in range(src_width):

                    # get and store rgb values from pixel [row][col]
                    (r,g,b,_) = src_img.get_at((col,row))


                    randx, randy = getRelativeRowColumn(row, col, (src_width, src_height), 
                                                        (resized_width, resized_height),
                                                        width_factor, height_factor,
                                                        xSpacing = 80)
                    

                    red_limit, blue_limit, green_limit = getRGBLimits(r, g, b, 15)


                    blue_dots = 0
                    green_dots = 0
                    red_dots = 0
                    
                    while red_dots < red_limit :
                        pygame.draw.rect(screen, (r,g,b), (randx, randy, 1, 1))
                        red_dots += 1
                        
                    while green_dots < green_limit :
                        pygame.draw.rect(screen, (r,g,b), (randx,randy, 1, 1))
                        green_dots += 1
                    
                    while blue_dots < blue_limit :
                        pygame.draw.rect(screen, (r,g,b), (randx,randy, 1, 1))
                        blue_dots += 1                    


                pygame.display.update()

            alreadyDrawn = True
            
        pygame.display.update()

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()
                

            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.isClicked(POINTILISM_MOUSE_POS):
                    main_menu(screen)
                
                if QUIT_BUTTON.isClicked(POINTILISM_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        
        pygame.display.update()

# -------------------END OF POINTILISM FUCNTION ----------------------------


if __name__ == "__main__" :
    main_menu(SCREEN)